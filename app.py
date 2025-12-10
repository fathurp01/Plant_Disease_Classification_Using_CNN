from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from google import genai
from dotenv import load_dotenv
import numpy as np
import os

# --------------------------
#  LOAD .env
# --------------------------
load_dotenv()  # <<< WAJIB agar GEMINI_API_KEY terbaca

app = Flask(__name__)

# --------------------------
#  CONFIG
# --------------------------
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load model CNN
model = load_model("best_model.keras")

# Kelas penyakit
class_names = [
    "Tomato__Bacterial_spot",
    "Tomato__Early_blight",
    "Tomato__Late_blight",
    "Tomato__Leaf_Mold",
    "Tomato__Septoria_leaf_spot",
    "Tomato__Spider_mites_Two-spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__healthy"
]

IMG_SIZE = 224

# --------------------------
#  GEMINI SETUP
# --------------------------

# Ambil API Key dari .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Cek apakah sudah terbaca
if GEMINI_API_KEY is None:
    raise ValueError("❌ GEMINI_API_KEY tidak ditemukan! Pastikan ada di file .env")

client = genai.Client(api_key=GEMINI_API_KEY)


def get_treatment_recommendation(disease_name):
    prompt = f"""
    Kamu adalah asisten agronomi yang menjelaskan penyakit tanaman tomat dengan bahasa Indonesia yang jelas dan terstruktur.

    Penyakit: {disease_name}

    Buat jawaban dalam format **Markdown** dengan struktur PERSIS seperti ini (jangan tambahkan judul/section lain di luar yang disebutkan):

    Deskripsi
    Tuliskan 2–4 kalimat yang menjelaskan:
    - Penyebab utama penyakit
    - Gejala khas yang muncul di daun/buah/batang

    Cara Mengatasi
    Buat 4–7 poin tindakan yang praktis, misalnya:
    - Langkah awal yang harus dilakukan petani
    - Jenis fungisida/insektisida (sebutkan **nama bahan aktif**, bukan merek dagang)
    - Cara aplikasi (umum, tidak perlu dosis terlalu teknis)

    Tulis dalam bentuk bullet list, contoh:
    - ...
    - ...
    - ...

    Pencegahan
    Buat 3–6 poin pencegahan, misalnya:
    - Pengelolaan lahan
    - Pengaturan jarak tanam
    - Sanitasi kebun
    - Pemilihan benih tahan penyakit

    Tulis juga dalam bentuk bullet list:
    - ...
    - ...
    - ...

    Rekomendasi Tambahan
    Buat 2–5 poin, misalnya:
    - Tips monitoring rutin
    - Kondisi lingkungan yang perlu dihindari
    - Saran konsultasi dengan ahli/penyuluh

    Tulis juga dalam bentuk bullet list:
    - ...
    - ...
    - ...

    Ketentuan bahasa:
    - Gunakan bahasa sederhana dan mudah dipahami petani
    - Hindari istilah terlalu teknis, tetapi tetap akurat
    - Jangan menyebut merek dagang pestisida, hanya sebutkan bahan aktifnya

    Jangan menggunakan simbol-simbol seperti *
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# --------------------------
# ROUTES
# --------------------------

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    recommendation = None
    img_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file and file.filename:
            # Simpan file
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            img_path = f'/uploads/{filename}'

            # Preprocessing
            img = image.load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediksi CNN
            pred = model.predict(img_array)
            idx = np.argmax(pred)

            prediction = class_names[idx]
            confidence = float(pred[0][idx])

            # Jika tidak sehat → minta rekomendasi Gemini
            if "healthy" not in prediction.lower():
                recommendation = get_treatment_recommendation(prediction)
            else:
                recommendation = "Tanaman sehat! Tidak ada penanganan khusus yang diperlukan."

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        img_path=img_path,
        recommendation=recommendation
    )


if __name__ == "__main__":
    app.run(debug=True)
