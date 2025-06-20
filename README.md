# 🚴‍♂️ Bike Sharing Analysis & Visualization Dashboard

![Streamlit](https://img.shields.io/badge/Powered%20by-Streamlit-blue?logo=streamlit) ![Python](https://img.shields.io/badge/Made%20with-Python-green?logo=python) ![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-%234488c4)

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk mengeksplorasi dan menganalisis data penyewaan sepeda menggunakan **Python** dan disajikan dalam bentuk dashboard interaktif menggunakan **Streamlit**. Dataset yang digunakan berasal dari penyewaan sepeda di Washington D.C., yang terbagi menjadi dua:

* `day_df`: Data harian selama **731 hari**.
* `hour_df`: Data per jam dengan total **17.379 baris**.

Seluruh data telah melalui proses **cleaning**, tanpa missing value atau duplikasi, dan tipe data sudah sesuai.

🔗 **Akses Dashboard di sini:**
👉 [Streamlit App](https://analysis-data-dengan-python-9wrscwbe3gkrrdbfby67om.streamlit.app/)

---

## 📊 Insight Utama

Berikut beberapa temuan penting dari eksplorasi data:

1. **Jumlah peminjaman cenderung lebih tinggi pada hari libur**, terutama pada awal hingga pertengahan Desember. Namun, menjelang liburan akhir tahun, terjadi penurunan tajam.
2. **Suhu berkorelasi positif dengan jumlah peminjaman.** Saat suhu hangat, peminjaman meningkat secara signifikan.
3. **Musim gugur mencatat jumlah peminjaman tertinggi** dibanding musim lainnya.
4. **Sebagian besar hari menunjukkan jumlah peminjaman antara 4000–6000 unit.**
5. **Jumlah peminjaman dipengaruhi kuat oleh pengguna terdaftar** dan **suhu rata-rata.**
6. **Kelembapan dan kecepatan angin berdampak negatif** terhadap aktivitas peminjaman sepeda.

---

## 📈 Fitur Visualisasi

Visualisasi yang disajikan pada dashboard mencakup:

* 📅 **Perbandingan Hari Kerja vs Hari Libur**
* 🌡️ **Hubungan Suhu dengan Jumlah Peminjaman**
* 📦 **Distribusi Peminjaman Harian**
* 🍂 **Perbandingan Jumlah Peminjaman antar Musim**
* 🔥 **Heatmap Korelasi antar Fitur Numerik**

---

## 🛠️ Tools & Teknologi

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

1. **Clone repositori ini**:

```bash
git clone https://github.com/username/bike-sharing-visualization.git
cd bike-sharing-visualization
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Jalankan aplikasi Streamlit**:

```bash
streamlit run dashboard.py
```

---

## 📁 Struktur Folder

```
.
├── dashboard.py
├── hour.csv
├── day.csv
└── README.md
```
---

## 💡 Pengembangan Selanjutnya

* Menambahkan fitur filter interaktif per musim, jam, atau suhu.
* Integrasi model prediksi (misal: regresi linear atau time series forecasting).
* Menyediakan saran operasional bisnis berdasarkan tren data.

---

## 👨‍💻 Author

**\Aulia Khalfani Izzati**
*Enthusiast Data Analysis | Python Learner | Streamlit Builder*
📧 \[Email] | 💼 \[LinkedIn]

