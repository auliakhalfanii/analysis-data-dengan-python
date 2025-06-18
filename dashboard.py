import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup
st.set_page_config(page_title="📊 Dashboard Bike Sharing", layout="wide")
sns.set(style="whitegrid")

# Load dataset
@st.cache_data
def load_data():
    hour = pd.read_csv('hour.csv')
    df = pd.read_csv('day.csv')
    return hour, df

hour, df = load_data()

df['dteday'] = pd.to_datetime(df['dteday'])
df['day_type'] = df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan / Libur')
df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Sidebar
st.sidebar.title("📌 Navigasi Dashboard")
menu = st.sidebar.radio("Pilih Bagian", [
    "Overview",
    "Hari Kerja vs Libur",
    "Suhu & Peminjaman",
    "Distribusi Peminjaman",
    "Musim",
    "Korelasi Fitur"
])

st.title("🚲 Dashboard Bike Sharing Dataset")

# --- Overview ---
if menu == "Overview":
    st.markdown("Selamat datang di dashboard analisis dataset Bike Sharing.")
    st.markdown("Gunakan menu di sebelah kiri untuk menavigasi berbagai visualisasi dan insight.")

# --- Section 1: Jumlah Peminjaman Hari Kerja vs Libur (1 Bulan Terakhir) ---
elif menu == "Hari Kerja vs Libur":
    st.subheader("📈 Jumlah Peminjaman: Hari Kerja vs Hari Libur (1 Bulan Terakhir)")
    last_month = df['dteday'].max() - pd.DateOffset(days=30)
    last_month_df = df[df['dteday'] >= last_month]

    fig1, ax1 = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=last_month_df, x='dteday', y='cnt', hue='day_type', marker='o', ax=ax1)
    ax1.set_title('Tren Jumlah Peminjaman Sepeda')
    ax1.set_xlabel('Tanggal')
    ax1.set_ylabel('Jumlah Peminjaman')
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

# --- Section 2: Pengaruh Suhu terhadap Peminjaman (3 Bulan Terakhir) ---
elif menu == "Suhu & Peminjaman":
    st.subheader("🌡️ Pengaruh Suhu terhadap Jumlah Peminjaman (3 Bulan Terakhir)")
    last_3_months = df['dteday'].max() - pd.DateOffset(months=3)
    df_3months = df[df['dteday'] >= last_3_months]

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df_3months, x='temp', y='cnt', hue='season_label', palette='viridis', ax=ax2)
    ax2.set_title('Suhu vs Jumlah Peminjaman')
    ax2.set_xlabel('Suhu (Ternormalisasi)')
    ax2.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig2)

    corr_temp = df_3months[['temp', 'cnt']].corr().iloc[0, 1]
    st.info(f"🔗 Korelasi antara suhu dan jumlah peminjaman: **{corr_temp:.2f}**")

# --- Section 3: Distribusi Jumlah Peminjaman Harian ---
elif menu == "Distribusi Peminjaman":
    st.subheader("📊 Distribusi Jumlah Peminjaman Harian")
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['cnt'], bins=30, kde=True, color='skyblue', ax=ax3)
    ax3.set_title('Distribusi Jumlah Peminjaman Harian')
    ax3.set_xlabel('Jumlah Peminjaman')
    ax3.set_ylabel('Frekuensi')
    st.pyplot(fig3)

# --- Section 4: Jumlah Peminjaman per Musim ---
elif menu == "Musim":
    st.subheader("🍁 Jumlah Peminjaman per Musim")
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=df, x='season_label', y='cnt', palette='coolwarm', ax=ax4)
    ax4.set_title('Jumlah Peminjaman berdasarkan Musim')
    ax4.set_xlabel('Musim')
    ax4.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig4)

# --- Section 5: Korelasi antar Fitur Numerik ---
elif menu == "Korelasi Fitur":
    st.subheader("🧠 Heatmap Korelasi antar Fitur Numerik")
    corr_matrix = df[['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']].corr()
    fig5, ax5 = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax5)
    ax5.set_title('Korelasi antar Fitur Numerik')
    st.pyplot(fig5)
