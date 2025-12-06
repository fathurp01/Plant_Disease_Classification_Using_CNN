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
    Jelaskan informasi mengenai penyakit tanaman tomat berikut:

    Penyakit: {disease_name}

    Berikan output dengan format berikut:

    **Deskripsi Singkat**
    - (jelaskan)

    **Cara Mengatasi**
    - (buat poin-poin)

    **Pencegahan**
    - (buat poin-poin)

    **Rekomendasi Tambahan**
    - (buat poin-poin)

    Gunakan bahasa Indonesia yang mudah dipahami.
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
