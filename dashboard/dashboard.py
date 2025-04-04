import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

st.set_page_config(page_title="Dashboard Penyewaan Sepeda")

st.header('Dashboard Data Penyewaan Sepeda :sparkles:')

# Sidebar logo
st.sidebar.image("dashboard/bike-logo.png")

# Menu navigasi
menu = st.sidebar.selectbox("Pilih Data Analisis", ("Hari", "Jam", "Bulan", "Cuaca"))

if menu == "Hari":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari")

    day_rentals = day_df.groupby("day_of_week")["total_rentals"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(day_rentals.index, day_rentals.values, color="skyblue")

    max_idx = day_rentals.argmax()
    min_idx = day_rentals.argmin()
    bars[max_idx].set_color("green")
    bars[min_idx].set_color("red")

    for i, v in enumerate(day_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_xlabel("Hari")
    plt.xticks(rotation=30)
    st.pyplot(fig)

elif menu == "Jam":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Jam")

    hourly_rentals = hour_df.groupby("hour")["total_rentals"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    bars = ax.barh(hourly_rentals.index.astype(str), hourly_rentals.values, color="orange")

    for i, v in enumerate(hourly_rentals.values):
        ax.text(v + 1000, i, str(v), va='center', fontsize=6)

    ax.set_ylabel("Jam")
    ax.set_xlabel("Jumlah Penyewaan")
    st.pyplot(fig)

elif menu == "Bulan":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Bulan")

    monthly_rentals = day_df.groupby("month")["total_rentals"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(monthly_rentals.index, monthly_rentals.values, color="lightblue")

    max_idx = monthly_rentals.argmax()
    min_idx = monthly_rentals.argmin()
    bars[max_idx].set_color("green")
    bars[min_idx].set_color("red")

    for i, v in enumerate(monthly_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

elif menu == "Cuaca":
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Cuaca")

    weather_rentals = hour_df.groupby("weather_condition")["total_rentals"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 3))
    bars = ax.bar(weather_rentals.index.astype(str), weather_rentals.values, color="lightgreen")

    max_idx = weather_rentals.argmax()
    min_idx = weather_rentals.argmin()
    bars[max_idx].set_color("green")
    bars[min_idx].set_color("red")

    for i, v in enumerate(weather_rentals.values):
        ax.text(i, v + 1000, str(v), ha='center', va='bottom', fontsize=6)

    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)