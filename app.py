from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load model
model = load_model("best_model.keras")

# Daftar class sesuai urutan training
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

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    img_path = None

    if request.method == "POST":
        file = request.files["image"]

        if file:
            # Simpan gambar upload
            img_path = "static/uploads/" + file.filename
            file.save(img_path)

            # Preprocess
            img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediksi
            pred = model.predict(img_array)
            idx = np.argmax(pred)

            prediction = class_names[idx]
            confidence = float(pred[0][idx])

    return render_template("index.html", prediction=prediction, confidence=confidence, img_path=img_path)


if __name__ == "__main__":
    app.run(debug=True)
