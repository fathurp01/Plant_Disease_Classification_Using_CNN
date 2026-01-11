# 🌿 Plant Disease Classification Using CNN

Aplikasi web untuk mengklasifikasikan penyakit pada tanaman tomat menggunakan teknologi Convolutional Neural Network (CNN) dan AI Gemini untuk validasi gambar serta memberikan rekomendasi penanganan.

---

## 📋 Daftar Isi
- [Fitur](#-fitur)
- [Persyaratan Sistem](#-persyaratan-sistem)
- [Panduan Instalasi](#-panduan-instalasi)
  - [Langkah 1: Install Python](#langkah-1-install-python)
  - [Langkah 2: Download Proyek](#langkah-2-download-proyek-ada-2-cara)
  - [Langkah 3: Install Git (Opsional)](#langkah-3-install-git-opsional)
  - [Langkah 4: Install Library Python](#langkah-4-install-library-python)
  - [Langkah 5: Setup API Key Gemini](#langkah-5-setup-api-key-gemini)
  - [Langkah 6: Menjalankan Aplikasi](#langkah-6-menjalankan-aplikasi)
- [Cara Menggunakan Aplikasi](#-cara-menggunakan-aplikasi)
- [Troubleshooting](#-troubleshooting)
- [Penjelasan Struktur Proyek](#-penjelasan-struktur-proyek)

---

## ✨ Fitur

- 🔍 **Deteksi Otomatis**: Mendeteksi apakah gambar adalah daun tomat menggunakan Gemini AI
- 🎯 **Klasifikasi Penyakit**: Mengidentifikasi 7 jenis penyakit tomat dan kondisi sehat
- 💊 **Rekomendasi Penanganan**: Memberikan saran penanganan, pencegahan, dan rekomendasi berbahasa Indonesia
- 🖼️ **User-Friendly Interface**: Tampilan web yang mudah digunakan

### Jenis Penyakit yang Dapat Dideteksi:
1. Tomato Bacterial Spot (Bercak Bakteri)
2. Tomato Early Blight (Hawar Awal)
3. Tomato Late Blight (Hawar Akhir)
4. Tomato Leaf Mold (Jamur Daun)
5. Tomato Septoria Leaf Spot (Bercak Daun Septoria)
6. Tomato Spider Mites (Tungau Laba-laba)
7. Tomato Target Spot (Bercak Target)
8. Tomato Healthy (Sehat)

---

## 💻 Persyaratan Sistem

- **Sistem Operasi**: Windows 10/11, macOS, atau Linux
- **Python**: Versi 3.8 atau lebih baru
- **RAM**: Minimal 4GB (disarankan 8GB)
- **Koneksi Internet**: Diperlukan untuk mengunduh library dan menggunakan API Gemini

---

## 🚀 Panduan Instalasi

Ikuti langkah-langkah di bawah ini dengan teliti. Panduan ini dibuat untuk pemula yang belum pernah menggunakan Git atau Python sebelumnya.

---

### Langkah 1: Install Python

Python adalah bahasa pemrograman yang digunakan proyek ini.

#### Untuk Windows:
1. Buka browser dan kunjungi: https://www.python.org/downloads/
2. Klik tombol **Download Python** (versi terbaru)
3. Setelah file installer terdownload, buka file tersebut
4. ⚠️ **PENTING**: Centang kotak **"Add Python to PATH"** di bagian bawah
5. Klik **Install Now**
6. Tunggu hingga instalasi selesai
7. Klik **Close**

#### Untuk Mac:
1. Buka browser dan kunjungi: https://www.python.org/downloads/
2. Download installer untuk macOS
3. Buka file `.pkg` yang terdownload
4. Ikuti instruksi instalasi
5. Selesai

#### Verifikasi Instalasi Python:
1. Buka **Command Prompt** (Windows) atau **Terminal** (Mac/Linux)
   - **Windows**: Tekan tombol `Windows + R`, ketik `cmd`, tekan Enter
   - **Mac**: Tekan `Command + Space`, ketik `terminal`, tekan Enter
   
2. Ketik perintah berikut dan tekan Enter:
   ```bash
   python --version
   ```
   
3. Jika muncul tulisan seperti `Python 3.x.x`, berarti Python sudah terinstall dengan benar ✅

---

### Langkah 2: Download Proyek (Ada 2 Cara)

Pilih salah satu cara di bawah ini:

#### **Cara A: Download Langsung (Tanpa Git) - LEBIH MUDAH** ⭐

Ini cara termudah, cocok untuk pemula yang tidak ingin install Git.

1. Buka browser dan kunjungi: https://github.com/fathurp01/Plant_Disease_Classification_Using_CNN
2. Klik tombol hijau **"<> Code"**
3. Klik **"Download ZIP"**
4. Setelah file ZIP terdownload, cari file tersebut di folder **Downloads**
5. Klik kanan pada file ZIP → Pilih **"Extract All..."** atau **"Extract Here"**
6. Folder proyek akan muncul dengan nama `Plant_Disease_Classification_Using_CNN-master`
7. **Pindahkan folder ini** ke lokasi yang mudah diakses, misalnya:
   - `C:\Users\NamaAnda\Documents\Plant_Disease_Classification_Using_CNN-master`
8. Selesai! Lanjut ke Langkah 4

#### **Cara B: Menggunakan Git Clone** 🔧

Cara ini membutuhkan instalasi Git terlebih dahulu (lihat Langkah 3).

---

### Langkah 3: Install Git (Opsional)

⚠️ **Langkah ini hanya diperlukan jika Anda memilih Cara B (Git Clone)**

Git adalah tools untuk mendownload dan mengelola kode dari internet.

#### Untuk Windows:
1. Buka browser dan kunjungi: https://git-scm.com/download/win
2. Download akan otomatis dimulai (file bernama `Git-x.x.x-64-bit.exe`)
3. Buka file installer yang terdownload
4. Klik **Next** beberapa kali (gunakan pengaturan default)
5. Pada bagian "Adjusting your PATH environment", pilih **"Git from the command line and also from 3rd-party software"**
6. Klik **Next** hingga **Install**
7. Setelah selesai, klik **Finish**

#### Untuk Mac:
1. Buka **Terminal**
2. Ketik: `git --version`
3. Jika Git belum terinstall, Mac akan otomatis menawarkan untuk menginstallnya
4. Ikuti instruksi yang muncul

#### Verifikasi Instalasi Git:
```bash
git --version
```
Jika muncul versi Git (contoh: `git version 2.x.x`), berarti Git sudah terinstall ✅

#### Clone Proyek Menggunakan Git:
1. Buka **Command Prompt** atau **Terminal**
2. Pindah ke folder tempat Anda ingin menyimpan proyek, contoh:
   ```bash
   cd C:\Users\NamaAnda\Documents
   ```
   
3. Ketik perintah berikut dan tekan Enter:
   ```bash
   git clone https://github.com/fathurp01/Plant_Disease_Classification_Using_CNN.git
   ```
   
4. Tunggu hingga proses download selesai
5. Masuk ke folder proyek:
   ```bash
   cd Plant_Disease_Classification_Using_CNN
   ```

---

### Langkah 4: Install Library Python

Library adalah kumpulan kode yang dibutuhkan agar aplikasi bisa berjalan.

#### Langkah Detail:

1. **Buka Command Prompt atau Terminal**

2. **Masuk ke folder proyek**:
   
   Jika Anda download dengan Cara A (ZIP):
   ```bash
   cd C:\Users\NamaAnda\Documents\Plant_Disease_Classification_Using_CNN-master
   ```
   
   Jika Anda menggunakan Git Clone (Cara B):
   ```bash
   cd C:\Users\NamaAnda\Documents\Plant_Disease_Classification_Using_CNN
   ```
   
   💡 **Tips**: Ganti `C:\Users\NamaAnda\Documents\` dengan lokasi folder proyek Anda yang sebenarnya

3. **Install semua library yang dibutuhkan**:
   
   Ada 2 cara, pilih salah satu:
   
   **Cara A: Install Sekaligus (LEBIH MUDAH)** ⭐
   
   Ketik perintah ini untuk install semua library sekaligus:
   ```bash
   pip install -r requirements.txt
   ```
   
   Tunggu hingga selesai (sekitar 2-5 menit). Selesai! ✅
   
   **Cara B: Install Satu-per-Satu**
   
   Jika Cara A error, install satu per satu:
   
   ```bash
   pip install flask
   ```
   Tunggu hingga selesai, lalu lanjut:
   
   ```bash
   pip install tensorflow
   ```
   Tunggu hingga selesai (ini yang paling lama), lalu lanjut:
   
   ```bash
   pip install google-genai
   ```
   Tunggu hingga selesai, lalu lanjut:
   
   ```bash
   pip install python-dotenv
   ```
   Tunggu hingga selesai, lalu lanjut:
   
   ```bash
   pip install numpy
   ```
   Tunggu hingga selesai, lalu lanjut:
   
   ```bash
   pip install pillow
   ```

4. **Verifikasi Instalasi**:
   
   Setelah semua selesai, cek apakah library sudah terinstall:
   ```bash
   pip list
   ```
   
   Anda akan melihat daftar library yang terinstall. Pastikan ada:
   - flask
   - tensorflow
   - google-genai
   - python-dotenv
   - numpy
   - pillow

✅ Jika semua library sudah muncul, instalasi berhasil!

⚠️ **Jika ada error** "pip is not recognized":
- Tutup Command Prompt
- Buka kembali Command Prompt baru
- Coba lagi

---

### Langkah 5: Setup API Key Gemini

Aplikasi ini menggunakan Google Gemini AI untuk validasi gambar dan memberikan rekomendasi. Anda perlu mendapatkan API Key gratis.

#### Langkah Mendapatkan API Key:

1. **Buka browser** dan kunjungi: https://aistudio.google.com/app/apikey

2. **Login** menggunakan akun Google Anda

3. Klik tombol **"Create API Key"** atau **"Get API Key"**

4. Pilih project atau buat project baru

5. **Copy API Key** yang muncul (simpan di notepad sementara)

#### Langkah Setup di Proyek:

1. **Buka folder proyek** menggunakan File Explorer atau Finder

2. **Cari file `.env.example`** di folder proyek
   - File ini adalah template/contoh untuk konfigurasi

3. **Copy file `.env.example`** dan rename menjadi `.env`
   
   **Cara copy dan rename**:
   - **Windows**:
     - Klik kanan pada file `.env.example`
     - Pilih **Copy**
     - Klik kanan di area kosong → **Paste**
     - Klik kanan pada file yang baru → **Rename**
     - Ubah nama menjadi `.env` (hapus .example)
     - Tekan Enter
   
   - **Mac/Linux**:
     - Klik kanan file `.env.example` → **Duplicate**
     - Rename menjadi `.env`
   
   **ATAU buat file baru** bernama `.env` (jika belum ada .env.example):
   - **Windows**:
     - Buka Notepad
     - Ketik isi file (lihat langkah 4)
     - Klik **File** → **Save As**
     - Di bagian "File name", ketik: `.env` (dengan tanda kutip)
     - Di bagian "Save as type", pilih **All Files**
     - Simpan di folder proyek
   
   - **Mac/Linux**:
     - Buka TextEdit atau editor teks
     - Ketik isi file (lihat langkah 4)
     - Save dengan nama `.env` di folder proyek

4. **Buka file `.env`** dengan Notepad atau text editor

5. **Ganti API Key** dengan yang Anda dapatkan tadi:
   
   Dari:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   Menjadi (contoh):
   ```
   GEMINI_API_KEY=AIzaSyBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   
   ⚠️ **Ganti** `your_gemini_api_key_here` dengan API Key asli Anda

6. **Save file** dan tutup

✅ Setup API Key selesai!

---

### Langkah 6: Menjalankan Aplikasi

Sekarang saatnya menjalankan aplikasi!

1. **Pastikan Anda masih di folder proyek** di Command Prompt/Terminal
   
   Jika belum, masuk ke folder proyek:
   ```bash
   cd C:\Users\NamaAnda\Documents\Plant_Disease_Classification_Using_CNN-master
   ```

2. **Jalankan aplikasi** dengan perintah:
   ```bash
   python app.py
   ```

3. **Tunggu beberapa detik**. Anda akan melihat output seperti ini:
   ```
   * Running on http://127.0.0.1:5000
   * Running on http://192.168.x.x:5000
   ```

4. **Buka browser** (Chrome, Firefox, Edge, dll)

5. **Ketik di address bar**:
   ```
   http://127.0.0.1:5000
   ```
   atau
   ```
   localhost:5000
   ```

6. **Aplikasi sudah berjalan!** 🎉

---

## 📱 Cara Menggunakan Aplikasi

1. **Siapkan foto daun tomat** yang ingin Anda periksa
   - Pastikan foto cukup jelas
   - Fokus pada daun
   - Format: JPG, JPEG, atau PNG

2. **Klik tombol "Choose File"** atau "Pilih File"

3. **Pilih foto daun tomat** dari komputer Anda

4. **Klik tombol "Upload"** atau "Prediksi"

5. **Tunggu beberapa detik** untuk proses:
   - Validasi apakah gambar adalah daun tomat
   - Klasifikasi penyakit (jika valid)
   - Generate rekomendasi penanganan (jika sakit)

6. **Hasil akan muncul**:
   - Nama penyakit (jika ada)
   - Tingkat kepercayaan/confidence
   - Rekomendasi penanganan lengkap (deskripsi, cara mengatasi, pencegahan, dll)

---

## 🔧 Troubleshooting

### Problem: `python: command not found`
**Solusi**: 
- Python belum terinstall atau belum ditambahkan ke PATH
- Install ulang Python dan pastikan centang "Add Python to PATH"
- Restart Command Prompt/Terminal

### Problem: `pip: command not found`
**Solusi**:
- Coba gunakan `python -m pip` sebagai ganti `pip`
- Contoh: `python -m pip install flask`

### Problem: `ModuleNotFoundError: No module named 'flask'`
**Solusi**:
- Library belum terinstall
- Jalankan: `pip install flask` atau library yang disebutkan

### Problem: `GEMINI_API_KEY tidak ditemukan`
**Solusi**:
- File `.env` belum dibuat atau salah nama
- Pastikan file bernama `.env` (dengan titik di depan)
- Pastikan isi file benar: `GEMINI_API_KEY=your_actual_key`
- Letakkan file `.env` di folder yang sama dengan `app.py`

### Problem: Error saat install TensorFlow di Windows
**Solusi**:
- Pastikan Python versi 3.8-3.11 (TensorFlow belum support 3.12+)
- Install Microsoft Visual C++ Redistributable:
  https://aka.ms/vs/17/release/vc_redist.x64.exe

### Problem: Aplikasi lambat saat prediksi pertama kali
**Solusi**:
- Ini normal! TensorFlow perlu load model terlebih dahulu
- Prediksi berikutnya akan lebih cepat

### Problem: Port 5000 sudah digunakan
**Solusi**:
- Ubah port di file `app.py` (baris terakhir):
  ```python
  if __name__ == "__main__":
      app.run(debug=True, port=5001)
  ```
- Akses aplikasi di: `http://localhost:5001`

---

## 📁 Penjelasan Struktur Proyek

```
Plant_Disease_Classification_Using_CNN/
│
├── app.py                  # File utama aplikasi Flask
├── best_model.keras        # Model CNN yang sudah ditraining
├── requirements.txt        # Daftar library yang dibutuhkan
├── .env                    # File konfigurasi API Key (Anda yang buat, tidak ada di repo)
├── .env.example            # Template/contoh file .env
├── .gitignore             # File yang diabaikan Git
├── README.md              # Dokumentasi ini
│
├── templates/             # Folder template HTML
│   └── index.html         # Tampilan web aplikasi
│
└── uploads/               # Folder penyimpanan gambar yang diupload (otomatis dibuat)
```

### Penjelasan File Penting:

- **app.py**: Otak dari aplikasi, berisi logika untuk:
  - Menerima upload gambar
  - Validasi dengan Gemini AI
  - Klasifikasi dengan model CNN
  - Menampilkan hasil dan rekomendasi

- **best_model.keras**: Model yang sudah dilatih untuk mengenali penyakit tomat
  - Ukuran: ~80MB
  - Sudah terlatih dengan ribuan gambar daun tomat

- **requirements.txt**: Daftar semua library yang dibutuhkan
  - Install sekaligus dengan: `pip install -r requirements.txt`
  - Lebih praktis daripada install satu-per-satu

- **.env.example**: Template/contoh file konfigurasi
  - Copy file ini dan rename menjadi `.env`
  - Isi dengan API Key Gemini Anda yang sebenarnya

- **.env**: File rahasia yang berisi API Key (Anda yang buat)
  - ⚠️ File ini TIDAK ada di repository GitHub
  - ⚠️ Anda harus buat sendiri dengan copy dari `.env.example`
  - ⚠️ Jangan pernah share file ini ke orang lain
  - ⚠️ Jangan upload ke GitHub
  - 📍 **Letak file**: Simpan di folder yang sama dengan `app.py`e ini ke orang lain
  - ⚠️ Jangan upload ke GitHub

- **templates/index.html**: Tampilan web yang dilihat pengguna

---

## 📝 Catatan Tambahan

### Menutup Aplikasi:
- Tekan `Ctrl + C` di Command Prompt/Terminal tempat aplikasi berjalan
- Atau tutup jendela Command Prompt/Terminal

### Menjalankan Ulang:
- Buka Command Prompt/Terminal
- Masuk ke folder proyek
- Jalankan: `python app.py`

### Update Proyek (Jika Ada Versi Baru):
Jika menggunakan Git:
```bash
git pull origin master
```

Jika download ZIP:
- Download ulang ZIP dari GitHub
- Extract dan replace folder lama

---

## 🤝 Kontribusi

Proyek ini dikembangkan untuk membantu petani tomat mendeteksi penyakit lebih awal. Jika Anda menemukan bug atau punya saran, silakan hubungi developer atau buat issue di GitHub.

---

## 📄 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan membantu petani.

---

## 👨‍💻 Developer

Dikembangkan oleh: **fathurp01**

GitHub: https://github.com/fathurp01/Plant_Disease_Classification_Using_CNN

---

## ❓ Butuh Bantuan?

Jika Anda mengalami kesulitan:
1. Baca ulang bagian Troubleshooting
2. Pastikan semua langkah sudah diikuti dengan benar
3. Periksa kembali instalasi Python dan library
4. Pastikan API Key sudah benar

Selamat mencoba! 🌱🍅
