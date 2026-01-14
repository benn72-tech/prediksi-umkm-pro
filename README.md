# 🏪 Prediksi UMKM PRO  
### Aplikasi Web AI untuk Prediksi Harga & Penjualan UMKM

**Prediksi UMKM PRO** adalah aplikasi web berbasis **Artificial Intelligence (Machine Learning)**  
yang membantu pelaku **UMKM memprediksi harga atau penjualan** berdasarkan data historis dalam bentuk **CSV**.

Aplikasi ini dirancang **sederhana, praktis, dan mudah digunakan**, bahkan oleh UMKM yang belum familiar dengan teknologi AI.

---

## 🎯 Tujuan Aplikasi

- Membantu UMKM mengambil keputusan berbasis data
- Mengurangi risiko salah stok dan salah harga
- Memberikan gambaran prediksi masa depan dari data sebelumnya
- Menjadi contoh penerapan AI sederhana untuk UMKM

---

## 🚀 Fitur Utama

- ✅ Upload data CSV sendiri
- ✅ Data contoh otomatis jika tidak upload CSV
- ✅ Pilih kolom input (X) dan target (Y)
- ✅ Prediksi otomatis menggunakan Machine Learning
- ✅ Menampilkan akurasi model (R² Score)
- ✅ Prediksi manual dengan input angka
- ✅ Akses via HP & Laptop (24 jam)

---

## 🧠 Cara Kerja AI (Penjelasan Sederhana)

1. User meng-upload data penjualan / harga dalam bentuk CSV
2. User memilih:
   - Kolom input (misalnya: stok, modal, jumlah produksi)
   - Kolom target (misalnya: penjualan atau harga)
3. Sistem melatih model AI menggunakan **Random Forest Regressor**
4. AI belajar dari data lama
5. AI memprediksi nilai baru berdasarkan input terbaru

📌 Semakin rapi dan banyak data, hasil prediksi akan semakin baik.

---

## 📂 Struktur File Project

prediksi-umkm-pro/
│
├── app.py # Aplikasi utama Streamlit
├── data_umkm.csv # Data contoh UMKM
├── model_umkm.pkl # Model Machine Learning
├── requirements.txt # Library Python yang dibutuhkan
└── README.md # Dokumentasi proyek

yaml
Copy code

---

## 🛠️ Teknologi yang Digunakan

- Python
- Streamlit (Web App Framework)
- Pandas (Pengolahan Data)
- Scikit-learn (Machine Learning)
- Matplotlib
- Joblib

---

## ▶️ Cara Menjalankan Aplikasi (Lokal)

1. Install library:
```bash
pip install -r requirements.txt
Jalankan aplikasi:

bash
Copy code
streamlit run app.py
Buka browser:

arduino
Copy code
http://localhost:8501
🌐 Demo Online
👉 Akses Aplikasi Online: https://prediksi-harga-beni-pro.streamlit.app/

