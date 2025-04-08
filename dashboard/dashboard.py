import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

base_path = os.path.dirname(__file__)

# Load dataset
day_df = pd.read_csv(os.path.join(base_path, "day_clean.csv"))
hour_df = pd.read_csv(os.path.join(base_path, "hour_clean.csv"))

# Pastikan kolom tanggal bertipe datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Konversi kode musim menjadi label jika perlu
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
if day_df['season'].dtype != 'O':
    day_df['season'] = day_df['season'].map(season_map)
if hour_df['season'].dtype != 'O':
    hour_df['season'] = hour_df['season'].map(season_map)

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")
st.header('🚲 Dashboard Data Penyewaan Sepeda')

# Sidebar - Logo dan Navigasi
st.sidebar.image(os.path.join(base_path, "bike-logo.png"))
menu = st.sidebar.selectbox("Pilih Data Analisis", ("Hari", "Jam", "Bulan", "Cuaca"))

# Sidebar - Fitur Interaktif
st.sidebar.markdown("### Filter Interaktif")

# Pilih musim
available_seasons = day_df['season'].dropna().unique().tolist()
season_selected = st.sidebar.multiselect("Pilih Musim:", available_seasons, default=available_seasons)

# Pilih rentang tanggal
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()
date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter dataframe berdasarkan interaksi
filtered_day_df = day_df[
    (day_df['season'].isin(season_selected)) &
    (day_df['dteday'] >= pd.to_datetime(date_range[0])) &
    (day_df['dteday'] <= pd.to_datetime(date_range[1]))
]

filtered_hour_df = hour_df[
    (hour_df['season'].isin(season_selected)) &
    (hour_df['dteday'] >= pd.to_datetime(date_range[0])) &
    (hour_df['dteday'] <= pd.to_datetime(date_range[1]))
]

# Visualisasi berdasarkan pilihan menu
if menu == "Hari":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari")
    
    day_order = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_rentals = filtered_day_df.groupby("day_of_week")["total_rentals"].sum().reindex(day_order)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(day_rentals.index, day_rentals.values, color="skyblue")

    for i, v in enumerate(day_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_xlabel("Hari")
    plt.xticks(rotation=30)
    st.pyplot(fig)

elif menu == "Jam":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Jam")

    hourly_rentals = filtered_hour_df.groupby("hour")["total_rentals"].sum()

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(hourly_rentals.index.astype(str), hourly_rentals.values, color="skyblue")

    for i, v in enumerate(hourly_rentals.values):
        ax.text(v + 1000, i, str(v), va='center', fontsize=6)

    ax.set_ylabel("Jam")
    ax.set_xlabel("Jumlah Penyewaan")
    st.pyplot(fig)

elif menu == "Bulan":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Bulan")

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    monthly_rentals = filtered_day_df.groupby("month")["total_rentals"].sum().reindex(month_order)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(monthly_rentals.index.astype(str), monthly_rentals.values, color="skyblue")

    for i, v in enumerate(monthly_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

elif menu == "Cuaca":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

    weather_rentals = filtered_hour_df.groupby("weather_condition")["total_rentals"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(weather_rentals.index.astype(str), weather_rentals.values, color="skyblue")

    for i, v in enumerate(weather_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    plt.xticks(rotation=30)
    st.pyplot(fig)
