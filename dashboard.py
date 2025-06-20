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
    return pd.read_csv('day.csv')

df = load_data()

# Preprocessing
df['dteday'] = pd.to_datetime(df['dteday'])
df['day_type'] = df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan / Libur')
df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['temp_group'] = pd.cut(df['temp'], bins=5)

# Sidebar
st.sidebar.title("📌 Navigasi Dashboard")
menu = st.sidebar.radio("Pilih Bagian", [
    "Overview",
    "Hari Kerja vs Libur",
    "Suhu & Peminjaman",
    "Distribusi Peminjaman",
    "Musim & Peminjaman",
    "Distribusi Fitur"
])

# Filter Sidebar
st.sidebar.markdown("### 🎛️ Filter Data")
start_date = st.sidebar.date_input("Mulai tanggal", df['dteday'].min().date())
end_date = st.sidebar.date_input("Akhir tanggal", df['dteday'].max().date())
season_filter = st.sidebar.multiselect("Pilih Musim", df['season_label'].unique(), default=df['season_label'].unique())

filtered_df = df[(df['dteday'] >= pd.to_datetime(start_date)) &
                 (df['dteday'] <= pd.to_datetime(end_date)) &
                 (df['season_label'].isin(season_filter))]

st.title("🚲 Dashboard Bike Sharing Dataset")

# --- Overview ---
if menu == "Overview":
    st.markdown("Selamat datang di dashboard analisis dataset Bike Sharing.")
    st.markdown("Gunakan menu di sebelah kiri untuk menavigasi berbagai visualisasi dan insight berdasarkan histogram.")

# --- Section 1: Hari Kerja vs Libur (Histogram) ---
elif menu == "Hari Kerja vs Libur":
    st.subheader("📊 Distribusi Peminjaman: Hari Kerja vs Hari Libur (1 Bulan Terakhir)")
    last_month_df = df[df['dteday'] >= '2012-12-01']
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=last_month_df, x='cnt', hue='day_type', bins=15, kde=True, palette='Set2', element='step', ax=ax)
    ax.set_title("Distribusi Jumlah Peminjaman - Hari Kerja vs Libur (Desember 2012)")
    ax.set_xlabel("Jumlah Peminjaman")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

# --- Section 2: Suhu & Peminjaman ---
elif menu == "Suhu & Peminjaman":
    st.subheader("🌡️ Distribusi Jumlah Peminjaman berdasarkan Kelompok Suhu (3 Bulan Terakhir)")
    last_3_months = df['dteday'].max() - pd.DateOffset(months=3)
    df_3months = df[df['dteday'] >= last_3_months]
    df_3months['temp_group'] = pd.cut(df_3months['temp'], bins=5)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=df_3months, x='cnt', hue='temp_group', bins=30, palette='coolwarm', element='step', kde=True, ax=ax)
    ax.set_title("Distribusi Jumlah Peminjaman Sepeda per Kelompok Suhu")
    ax.set_xlabel("Jumlah Peminjaman")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

# --- Section 3: Distribusi Jumlah Peminjaman Harian ---
elif menu == "Distribusi Peminjaman":
    st.subheader("📊 Distribusi Jumlah Peminjaman Harian")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(filtered_df['cnt'], bins=30, kde=True, color='skyblue', ax=ax)
    ax.set_title("Distribusi Jumlah Peminjaman Harian")
    ax.set_xlabel("Jumlah Peminjaman")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

# --- Section 4: Musim & Peminjaman ---
elif menu == "Musim & Peminjaman":
    st.subheader("🍁 Distribusi Peminjaman berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=filtered_df, x='cnt', hue='season_label', bins=30, kde=True, element='step', palette='Spectral', ax=ax)
    ax.set_title("Distribusi Jumlah Peminjaman per Musim")
    ax.set_xlabel("Jumlah Peminjaman")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)

# --- Section 5: Distribusi Fitur Numerik Terhadap Peminjaman ---
elif menu == "Distribusi Fitur":
    st.subheader("📈 Distribusi Fitur Numerik terhadap Jumlah Peminjaman")
    fitur = st.selectbox("Pilih Fitur Numerik", ['temp', 'atemp', 'hum', 'windspeed'])
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(data=filtered_df, x=fitur, weights=filtered_df['cnt'], bins=30, color='salmon', ax=ax)
    ax.set_title(f"Distribusi Terbobot: {fitur} terhadap Jumlah Peminjaman")
    ax.set_xlabel(fitur)
    ax.set_ylabel("Total Peminjaman (terbobot)")
    st.pyplot(fig)
