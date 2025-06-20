# 🚴‍♂️ Bike Sharing Analysis & Visualization Dashboard

![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-blue?logo=streamlit)
![Python](https://img.shields.io/badge/Made%20with-Python-green?logo=python)
![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-%234488c4)

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda di Washington D.C. menggunakan **Python** dan menyajikannya dalam bentuk dashboard interaktif menggunakan **Streamlit**.

Dataset terdiri dari dua bagian:
- `day.csv` : Data harian peminjaman sepeda.
- `hour.csv` : Data per jam (belum digunakan dalam visualisasi saat ini).

Seluruh data telah dibersihkan dan siap dianalisis tanpa missing value atau duplikasi.

🔗 **Demo Dashboard Streamlit:**  
👉 [Streamlit App](https://analysis-data-dengan-python-9wrscwbe3gkrrdbfby67om.streamlit.app/)

---

## 📊 Insight Utama

1. **Hari kerja menunjukkan jumlah peminjaman lebih tinggi dan stabil** dibanding hari libur.
2. **Peminjaman tertinggi terjadi saat suhu sedang hingga hangat (0.4–0.6)**.
3. **Distribusi peminjaman harian paling sering berada antara 4000–6000.**
4. **Musim gugur mencatatkan aktivitas peminjaman terbanyak.**
5. **Pengguna terdaftar dan suhu rata-rata sangat mempengaruhi jumlah peminjaman.**

---

## 📈 Fitur Visualisasi

Visualisasi yang tersedia:
- 📊 Histogram Jumlah Peminjaman: Hari Kerja vs Libur
- 🌡️ Distribusi Jumlah Peminjaman Berdasarkan Suhu
- 📦 Distribusi Jumlah Peminjaman Harian
- 🍂 Distribusi Jumlah Peminjaman per Musim
- ⚙️ Distribusi Terbobot Fitur Numerik terhadap Jumlah Peminjaman

Semua visualisasi disusun menggunakan **Seaborn + Matplotlib** dan berjenis **histogram** sesuai analisis notebook.

---

## 🎛️ Fitur Interaktif

Dashboard dilengkapi fitur filter:
- Filter **tanggal** (start-end)
- Filter **musim (season)**
- Pemilihan **fitur numerik** untuk analisis terbobot

---

## 🛠️ Teknologi

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn

---

## 🚀 Menjalankan Proyek Secara Lokal

1. **Clone repositori ini:**
```bash
git clone https://github.com/username/bike-sharing-visualization.git
cd bike-sharing-visualization
```

2. **Install dependensi:**
```bash
pip install -r requirements.txt
```

3. **Jalankan Streamlit App:**
```bash
streamlit run dashboard_bike_sharing.py
```

---

## 📁 Struktur Folder

```
.
├── dashboard_bike_sharing.py
├── day.csv
├── hour.csv
├── requirements.txt
└── README.md
```

---

## 💡 Pengembangan Selanjutnya

- Analisis tambahan dari `hour.csv`
- Prediksi jumlah peminjaman (regresi/time series)
- Visualisasi berbasis peta jika tersedia data lokasi

---

## 👨‍💻 Author

**Aulia Khalfani Izzati**  
*Data Analysis Enthusiast | Python Learner | Streamlit Builder*  
📧 [Email] | 💼 [LinkedIn]
