# -*- coding: utf-8 -*-
"""proyek-analisis-data-bike-sharing-dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZvxbLZKJJZpy3ZC5tEiwFm_9YI360owQ

# Proyek Analisis Data: Bike Sharing Dataset
- **Nama:** Nanda Arya Putra
- **Email:** nandaarya404@gmail.com
- **ID Dicoding:** Nanda Arya Putra

## Menentukan Pertanyaan Bisnis

1. Pada hari apa saja terjadi penyewaan sepeda tertinggi dan terendah ?
2. Pada jam berapa saja terjadi penyewaan sepeda tertinggi dan terendah ?
3. Pada bulan apa saja terjadi penyewaan sepeda tertinggi dan terendah ?
4. Pada kondisi cuaca apa saja terjadi penyewaan sepeda tertinggi dan terendah ?

## Import Semua Packages/Library yang Digunakan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""## Data Wrangling

### Gathering Data
Get and load Bike Sharing Dataset from https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset
"""

# Create day dataframe
day_df = pd.read_csv("/kaggle/input/bike-sharing-dataset/day.csv")
day_df.head()

"""**Insight:**

Berikut adalah penjelasan fungsi dari setiap kolom dalam dataframe **day_df**:

- Informasi Identitas & Waktu
    - instant → Indeks unik untuk setiap record.
    - dteday → Tanggal pencatatan data.
    - season → Musim dalam setahun (1: Spring, 2: Summer, 3: Fall, 4: Winter).
    - yr → Tahun pengambilan data (0: 2011, 1: 2012).
    - mnth → Bulan pengambilan data (1–12).
    - weekday → Hari dalam seminggu (0: Minggu, 6: Sabtu).

- Informasi Hari Khusus
    - holiday → Menandakan apakah hari tersebut libur nasional (1: Libur, 0: Tidak).
    - workingday → Menandakan apakah hari tersebut hari kerja (1: Ya, 0: Tidak, yaitu akhir pekan atau libur).

- Informasi Cuaca & Lingkungan
    - weathersit → Kondisi cuaca (1: Cerah, 2: Berkabut, 3: Hujan ringan/salju ringan, 4: Hujan/salju lebat).
    - temp → Suhu yang sudah dinormalisasi berdasarkan rentang -8°C hingga 39°C.
    - atemp → Suhu yang dirasakan (feels like) dalam skala normalisasi -16°C hingga 50°C.
    - hum → Tingkat kelembapan yang dinormalisasi (0–1).
    - windspeed → Kecepatan angin yang dinormalisasi berdasarkan nilai maksimum 67.

- Informasi Pengguna & Jumlah Penyewaan
    - casual → Jumlah pengguna yang tidak terdaftar (pengguna kasual).
    - registered → Jumlah pengguna yang terdaftar.
    - cnt → Total penyewaan sepeda (gabungan dari casual + registered).
"""

# Create hour dataframe
hour_df = pd.read_csv("/kaggle/input/bike-sharing-dataset/hour.csv")
hour_df.head()

"""**Insight:**

Berikut adalah penjelasan fungsi dari setiap kolom dalam dataframe **hour_df**:

- Informasi Identitas & Waktu
    - instant → Indeks unik untuk setiap record.
    - dteday → Tanggal pencatatan data.
    - season → Musim dalam setahun (1: Spring, 2: Summer, 3: Fall, 4: Winter).
    - yr → Tahun pengambilan data (0: 2011, 1: 2012).
    - mnth → Bulan pengambilan data (1–12).
    - hr → Jam pengambilan data (hanya ada di hour.csv, 0–23).
    - weekday → Hari dalam seminggu (0: Minggu, 6: Sabtu).

- Informasi Hari Khusus
    - holiday → Menandakan apakah hari tersebut libur nasional (1: Libur, 0: Tidak).
    - workingday → Menandakan apakah hari tersebut hari kerja (1: Ya, 0: Tidak, yaitu akhir pekan atau libur).

- Informasi Cuaca & Lingkungan
    - weathersit → Kondisi cuaca (1: Cerah, 2: Berkabut, 3: Hujan ringan/salju ringan, 4: Hujan/salju lebat).
    - temp → Suhu yang sudah dinormalisasi berdasarkan rentang -8°C hingga 39°C.
    - atemp → Suhu yang dirasakan (feels like) dalam skala normalisasi -16°C hingga 50°C.
    - hum → Tingkat kelembapan yang dinormalisasi (0–1).
    - windspeed → Kecepatan angin yang dinormalisasi berdasarkan nilai maksimum 67.

- Informasi Pengguna & Jumlah Penyewaan
    - casual → Jumlah pengguna yang tidak terdaftar (pengguna kasual).
    - registered → Jumlah pengguna yang terdaftar.
    - cnt → Total penyewaan sepeda (gabungan dari casual + registered).

### Assessing Data
Proses ini adalah menilai kualitas dari seluruh data yang akan digunakan. Penilaian ini bertujuan untuk melihat berbagai permasalahan yang ada dalam data tersebut.

#### Memeriksa tipe data pada DataFrame day_df dan hour_df
"""

print(day_df.info(), "\n")
print(hour_df.info(), "\n")

"""**Insight:**

- day_df memiliki 731 baris, yang berarti dataset ini menyajikan data harian selama sekitar dua tahun.
- hour_df memiliki 17.379 baris, yang berarti dataset ini menyajikan data per jam untuk periode yang sama.
- Kedua dataset memiliki kolom yang mirip, tetapi hour_df memiliki tambahan kolom hr (jam), yang masuk akal karena dataset ini mencatat peminjaman sepeda dalam skala jam.
- Kolom dteday bertipe object (string), bukan tipe datetime. Disarankan untuk mengubahnya menjadi datetime64 untuk mempermudah analisis waktu.
- Sebagian besar kolom memiliki tipe int64, yang menunjukkan data kategorikal atau diskrit.
- Kolom temp, atemp, hum, dan windspeed memiliki tipe float64, yang menunjukkan data kontinu.

#### Memeriksa missing values pada DataFrame day_df dan hour_df
"""

print("Jumlah missing values pada day_df: \n", day_df.isna().sum(), "\n")
print("Jumlah missing values pada hour_df", hour_df.isna().sum(), "\n")

"""**Insight:**

- Tidak ada missing values pada dataframe day_df dan hour_df

#### Memeriksa data duplicate pada DataFrame day_df dan hour_df
"""

print("Jumlah duplikasi pada day_df: ", day_df.duplicated().sum())
print("Jumlah duplikasi pada hour_df: ", hour_df.duplicated().sum())

"""**Insight:**

- Tidak ada duplikasi data pada dataframe day_df dan hour_df

#### Memeriksa parameter statistik dari kolom numerik pada DataFrame day_df dan hour_df
"""

day_df.describe()

hour_df.describe()

"""**Insight:**

1. Dataset Harian (day_df)
- Distribusi Penyewaan (cnt):
    - Rata-rata: 4.504 sepeda/hari, maksimum 8.714 sepeda/hari.
    - Distribusi tidak merata, terlihat dari standar deviasi yang tinggi (1.937).

- Variasi Cuaca (temp, atemp, hum, windspeed):
    - Suhu rata-rata 0.49 (skala 0-1), dengan variasi cukup lebar.
    - Kelembaban (hum) memiliki rentang luas, dari 0% hingga 97%.

- Sebaran Musim dan Bulan:
    - Data tersebar merata di semua musim (season: 1-4) dan bulan (mnth: 1-12).

2. Dataset Per Jam (hour_df)
- Distribusi Penyewaan Per Jam (cnt):
    - Rata-rata 189 sepeda/jam, tetapi maksimum mencapai 977 sepeda/jam.
    - Variasi tinggi terlihat dari standar deviasi (181).

- Tren Jam (hr):
    - Rata-rata jam 11.54, menunjukkan lebih banyak penyewaan di siang hari.

- Kondisi Cuaca (temp, hum, windspeed):
    - Suhu (temp) lebih luas rentangnya dibanding dataset harian.
    - Beberapa jam memiliki kelembaban hingga 100% dan angin sangat rendah (windspeed = 0).

- Perbedaan Penyewaan casual vs registered:
    - Penyewa terdaftar (registered) jauh lebih banyak dibanding penyewa kasual (casual).
    - Maksimum registered 886/jam, sedangkan casual hanya 367/jam.

### Cleaning Data

- Menghapus kolom instant karena tidak diperlukan
- Mengubah tipe data kolom 'season', 'mnth', 'holiday', 'weekday', 'weathersit' dari int64 menjadi category karena hanya berisi beberaba varian value saja
- Mengubah tipe data dteday dari object menjadi datetime karena lebih cocok untuk tipe data tanggal
- Mengubah nama kolom agar lebih mudah dipahami
- Mengkonversi isi kolom kategori dari nilai numerik ke nilai asli agar mudah dipahami

#### Menghapus kolom instant
"""

hour_df.drop(['instant'], axis = 1, inplace= True)
day_df.drop(['instant'], axis = 1, inplace= True)

print(day_df.info(), "\n")
print(hour_df.info(), "\n")

"""**Insight:**
- Kolom instant telah terhapus dari dataframe day_df dan hour_df

#### Mengubah tipe data kolom 'season', 'mnth', 'holiday', 'weekday', 'weathersit' dari int64 menjadi category
"""

columns = ['season', 'mnth', 'holiday', 'weekday', 'weathersit']

for column in columns:
    day_df[column] =  day_df[column].astype("category")
    hour_df[column] =  hour_df[column].astype("category")

print(day_df.info(), "\n")
print(hour_df.info(), "\n")

"""**Insight:**
- Tipe data kolom 'season', 'mnth', 'holiday', 'weekday', 'weathersit' dari dataframe day_df dan hour_df sudah berubah dari int64 menjadi category

#### Mengubah tipe data dteday dari object menjadi datetime
"""

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

print(day_df.info(), "\n")
print(hour_df.info(), "\n")

"""**Insight:**
- Tipe data kolom 'dteday' dari dataframe day_df dan hour_df sudah berubah dari object menjadi datetime

#### Mengubah nama kolom agar lebih mudah dipahami
"""

# Rename day_df columns
day_df.rename(columns={
    'yr': 'year',
    'mnth': 'month',
    'weekday': 'day_of_week',
    'weathersit': 'weather_condition',
    'windspeed': 'wind_speed',
    'cnt': 'total_rentals',
    'hum': 'humidity'
}, inplace=True)

# Rename hour_df columns
hour_df.rename(columns={
    'yr': 'year',
    'hr': 'hour',
    'mnth': 'month',
    'weekday': 'day_of_week',
    'weathersit': 'weather_condition',
    'windspeed': 'wind_speed',
    'cnt': 'total_rentals',
    'hum': 'humidity'
}, inplace=True)

print(day_df.info(), "\n")
print(hour_df.info(), "\n")

"""**Insight:**
- Perubahan Nama Kolom untuk day_df
    - yr diubah menjadi year
    - mnth diubah menjadi month
    - weekday diubah menjadi day_of_week
    - weathersit diubah menjadi weather_condition
    - windspeed diubah menjadi wind_speed
    - cnt diubah menjadi total_rentals
    - hum diubah menjadi humidity
      
- Perubahan Nama Kolom untuk hour_df
    - yr diubah menjadi year
    - hr diubah menjadi hour
    - mnth diubah menjadi month
    - weekday diubah menjadi day_of_week
    - weathersit diubah menjadi weather_condition
    - windspeed diubah menjadi wind_speed
    - cnt diubah menjadi total_rentals
    - hum diubah menjadi humidity

#### Mengkonversi isi kolom kategori dari nilai numerik ke nilai asli
"""

season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
weather_map = {1: 'Clear', 2: 'Misty', 3: 'Light_rainsnow', 4: 'Heavy_rainsnow'}
day_of_week_map = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                   4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
year_map = {0: '2011', 1: '2012'}

day_df.replace({'season': season_map, 'month': month_map, 'weather_condition': weather_map,
                'day_of_week': day_of_week_map, 'year': year_map}, inplace=True)
hour_df.replace({'season': season_map, 'month': month_map, 'weather_condition': weather_map,
                 'day_of_week': day_of_week_map, 'year': year_map}, inplace=True)

"""**Insight:**
- Kolom season yang awalnya berisi angka (1 hingga 4) diubah menjadi nama musim, yaitu 'Spring', 'Summer', 'Fall', dan 'Winter'.
- Kolom month yang sebelumnya berisi angka (1 hingga 12) diubah menjadi nama bulan, yaitu 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', dan 'Dec'.
- Kolom weather_condition yang sebelumnya berisi angka (1 hingga 4) diubah menjadi kondisi cuaca, yaitu 'Clear', 'Misty', 'Light_rainsnow', dan 'Heavy_rainsnow'.
- Kolom day_of_week yang sebelumnya berisi angka (0 hingga 6) diubah menjadi nama hari dalam seminggu, yaitu 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', dan 'Saturday'.
- Kolom year, yang sebelumnya berisi nilai numerik (0 dan 1), diubah menjadi nama tahun, yaitu '2011' dan '2012'.

## Exploratory Data Analysis (EDA)

### Explore data day_df
"""

day_df.describe(include="all")

"""**Insight:**
- Total rata-rata penyewaan sepeda per hari adalah 4.504 unit, dengan standar deviasi 1.937 unit.
- Penyewaan sepeda minimum tercatat sebanyak 22 unit dalam satu hari, sementara maksimum mencapai 8.714 unit.
- Penyewaan rata-rata pengguna casual adalah 848 sepeda per hari, dengan standar deviasi 686.
- Penyewaan rata-rata pengguna terdaftar adalah 3.656 sepeda per hari, dengan standar deviasi 1.560.
- Musim yang paling sering muncul dalam data adalah Fall (musim gugur), dengan frekuensi 188 hari dari 731 hari.
- Hari yang paling sering tercatat adalah Minggu (Sunday), muncul sebanyak 105 kali.
- Kondisi cuaca yang paling umum adalah "Clear" (Cerah), dengan frekuensi 463 hari dari total 731 hari.
- Suhu rata-rata (temp) adalah 0.495 (nilai normalisasi), dengan rentang antara 0.059 hingga 0.862.
- Kelembaban rata-rata adalah 0.628, dengan rentang dari 0 hingga 0.973.
- Kecepatan angin rata-rata adalah 0.190, dengan rentang dari 0.022 hingga 0.507.
"""

day_df.groupby("day_of_week")["total_rentals"].sum().sort_values(ascending=False)

"""**Insight:**
- Jumat (Friday) memiliki jumlah penyewaan tertinggi dengan 487,790 penyewaan. Ini menunjukkan banyak orang menyewa sepeda menjelang akhir pekan, mungkin untuk kegiatan luar ruangan atau beraktivitas di akhir pekan.
- Minggu (Sunday) memiliki jumlah penyewaan terendah dengan 444,027 penyewaan. Hal ini bisa jadi karena orang lebih memilih beristirahat di akhir pekan atau melakukan aktivitas lain yang tidak melibatkan sepeda.
- Penyewaan sepeda lebih tinggi pada hari kerja menjelang akhir pekan, terutama pada Jumat (487,790) dan Sabtu (477,807). Namun, pada Minggu, penyewaan menurun secara signifikan, dengan jumlah 444,027 penyewaan.
"""

day_df.groupby("month")["total_rentals"].sum().sort_values(ascending=False)

"""**Insight:**
- Agustus (August) memiliki jumlah penyewaan tertinggi dengan 351,194 penyewaan.
- Januari (January) memiliki jumlah penyewaan terendah dengan 134,933 penyewaan.
- Terdapat tren musiman yang jelas dalam data, dengan Agustus menjadi bulan dengan penyewaan tertinggi, dan Januari dengan penyewaan terendah, menunjukkan bahwa penyewaan sepeda lebih populer pada musim yang lebih hangat, sementara bulan-bulan yang lebih dingin memiliki penyewaan yang lebih sedikit.

### Explore data hour_df
"""

hour_df.describe(include="all")

"""**Insight:**
- Rata-rata penyewaan sepeda per jam adalah 189 unit, dengan standar deviasi 181 unit.
- Penyewaan sepeda minimum adalah 1 unit dalam satu jam, sedangkan maksimum mencapai 977 unit dalam satu jam.
- Rata-rata penyewaan oleh pengguna casual (tidak terdaftar) adalah 35 unit per jam, dengan standar deviasi 49 unit.
- Rata-rata penyewaan oleh pengguna terdaftar adalah 153 unit per jam, dengan standar deviasi 151 unit.
- Musim yang paling sering muncul dalam data adalah Fall (musim gugur), dengan total 4.496 observasi.
- Bulan yang paling sering tercatat adalah Mei (May), dengan total 1.488 observasi.
- Hari yang paling sering tercatat adalah Sabtu (Saturday), dengan frekuensi 2.512 observasi.
- Peminjaman sepeda rata-rata terjadi pada jam 11.54 (sekitar pukul 11:30 siang).
- Peminjaman sepeda paling sedikit terjadi pada jam 00:00 (tengah malam), sementara puncak peminjaman terjadi pada jam 23:00.
- Kondisi cuaca paling umum adalah "Clear" (Cerah), dengan 11.413 observasi.
- Suhu rata-rata (temp) adalah 0.497 (nilai normalisasi), dengan rentang dari 0.020 hingga 1.000.
- Kelembaban rata-rata adalah 0.627, dengan rentang dari 0 hingga 1.000.
- Kecepatan angin rata-rata adalah 0.190, dengan rentang dari 0.022 hingga 0.850.
"""

hour_df.groupby("hour")["total_rentals"].sum().sort_values(ascending=False)

"""**Insight:**
- Pukul 17:00 (336.860 penyewaan) dan 18:00 (309.772 penyewaan) adalah jam dengan penyewaan sepeda tertinggi. Ini kemungkinan terjadi karena jam pulang kerja, di mana banyak orang menggunakan sepeda sebagai alat transportasi.
- Pukul 08:00 (261.001 penyewaan) juga memiliki jumlah penyewaan tinggi, menunjukkan bahwa pagi hari adalah waktu sibuk, mungkin untuk perjalanan ke tempat kerja atau sekolah.
- Pukul 03:00 (8.174 penyewaan) dan 04:00 (4.428 penyewaan) memiliki penyewaan paling sedikit. Ini wajar karena waktu ini termasuk dini hari, di mana aktivitas masyarakat sangat minim.
- Tren penyewaan sepeda menunjukkan dua puncak utama, yaitu pagi (sekitar pukul 08:00) dan sore (sekitar pukul 17:00 - 18:00), kemungkinan besar terkait dengan mobilitas pekerja dan pelajar. Penyewaan cenderung rendah pada malam hingga dini hari (pukul 00:00 - 05:00), sesuai dengan pola aktivitas manusia yang lebih sedikit pada jam-jam tersebut.
"""

hour_df.groupby("weather_condition")["total_rentals"].sum()

"""**Insight:**
- Cuaca cerah atau sedikit berawan (2.338.173 penyewaan) memiliki jumlah penyewaan tertinggi. Ini menunjukkan bahwa kondisi cuaca yang baik sangat mendukung aktivitas bersepeda.
- Cuaca berkabut atau mendung (795.952 penyewaan) masih memiliki angka penyewaan cukup tinggi, meskipun lebih rendah dibandingkan cuaca cerah. Orang tetap menggunakan sepeda meskipun kondisi tidak terlalu ideal.
- Hujan ringan atau salju ringan (158.331 penyewaan) menunjukkan penurunan signifikan dibandingkan cuaca cerah atau berkabut. Kemungkinan karena kenyamanan dan keselamatan yang berkurang saat hujan atau salju turun.
- Hujan deras, badai petir, es, atau kabut tebal (223 penyewaan) memiliki angka penyewaan paling rendah. Ini wajar karena kondisi cuaca ekstrem membuat bersepeda menjadi berbahaya dan tidak nyaman.
- Penyewaan sepeda paling tinggi saat cuaca cerah dan menurun seiring memburuknya kondisi cuaca.

## Visualization & Explanatory Analysis

### Pertanyaan 1: Pada hari apa saja terjadi penyewaan sepeda tertinggi dan terendah ?
"""

import matplotlib.pyplot as plt

# Kelompokkan dan urutkan berdasarkan total_rentals
day_rentals = day_df.groupby("day_of_week")["total_rentals"].sum()

# Membuat diagram batang
plt.figure(figsize=(10,6))
bars = plt.bar(day_rentals.index, day_rentals.values, color='gray')

# Menambahkan label jumlah di atas batang
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(int(height)), ha='center', va='bottom', fontsize=10)

# Memberi label dan judul
plt.xlabel('Hari dalam Minggu')
plt.ylabel('Total Penyewaan Sepeda')
plt.title('Total Penyewaan Sepeda Berdasarkan Hari')

# Menampilkan diagram
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""**Insight:**
Kesimpulan dari data di atas menunjukkan bahwa penyewaan sepeda tertinggi terjadi pada hari Jumat, dengan 487,790 penyewaan, yang mengindikasikan aktivitas luar ruangan yang meningkat menjelang akhir pekan. Sementara itu, penyewaan sepeda terendah tercatat pada hari Minggu dengan 444,027 penyewaan, mungkin karena orang lebih memilih beristirahat atau melakukan kegiatan lain. Secara keseluruhan, hari kerja menjelang akhir pekan cenderung memiliki tingkat penyewaan yang lebih tinggi.

### Pertanyaan 2: Pada jam berapa saja terjadi penyewaan sepeda tertinggi dan terendah ?
"""

import matplotlib.pyplot as plt

# Data yang dihasilkan oleh kode sebelumnya
hourly_rentals = hour_df.groupby("hour")["total_rentals"].sum()

# Membuat diagram batang horizontal
plt.figure(figsize=(10, 6))
hourly_rentals.plot(kind='barh', color='skyblue')

# Menambahkan judul dan label
plt.title('Total Penyewaan Sepeda per Jam', fontsize=14)
plt.xlabel('Total Penyewaan', fontsize=12)
plt.ylabel('Jam', fontsize=12)

# Menambahkan label di ujung setiap batang
for index, value in enumerate(hourly_rentals):
    plt.text(value, index, str(value), va='center', ha='left', fontsize=10)

# Menampilkan diagram
plt.show()

"""**Insight:**
Pada jam 17:00 dan 18:00 terjadi penyewaan sepeda tertinggi, dengan masing-masing mencapai 336.860 dan 309.772 penyewaan, yang kemungkinan besar disebabkan oleh jam pulang kerja. Sebaliknya, penyewaan sepeda terendah terjadi pada pukul 03:00 dan 04:00, dengan hanya 8.174 dan 4.428 penyewaan, yang wajar karena waktu tersebut merupakan dini hari dengan aktivitas yang minim. Secara keseluruhan, tren menunjukkan dua puncak utama di pagi hari (sekitar pukul 08:00) dan sore hari (pukul 17:00 - 18:00), serta penurunan tajam pada malam hingga dini hari.

### Pertanyaan 3: Pada bulan apa saja terjadi penyewaan sepeda tertinggi dan terendah ?
"""

import matplotlib.pyplot as plt

# Data per bulan
monthly_rentals = day_df.groupby("month")["total_rentals"].sum()

# Membuat diagram batang vertikal
plt.figure(figsize=(10, 6))
monthly_rentals.plot(kind='bar', color='skyblue')

# Menambahkan label dan judul
plt.title('Total Penyewaan Sepeda per Bulan', fontsize=16)
plt.xlabel('Bulan', fontsize=12)
plt.ylabel('Total Penyewaan', fontsize=12)

# Menambahkan label jumlah di atas batang
for i, value in enumerate(monthly_rentals):
    plt.text(i, value + 5000, str(value), ha='center', va='bottom', fontsize=10)

# Menampilkan diagram
plt.xticks(rotation=45)
plt.show()

"""**Insight:**
Berdasarkan data, bulan dengan penyewaan sepeda tertinggi adalah Agustus (351,194 penyewaan), sementara bulan dengan penyewaan sepeda terendah adalah Januari (134,933 penyewaan). Ini menunjukkan adanya fluktuasi musiman dalam penyewaan sepeda, di mana bulan-bulan dengan cuaca lebih hangat, seperti Agustus, mengalami jumlah penyewaan yang lebih tinggi, sedangkan pada bulan-bulan yang lebih dingin, seperti Januari, jumlah penyewaan cenderung menurun.

### Pertanyaan 4: Pada kondisi cuaca apa saja terjadi penyewaan sepeda tertinggi dan terendah ?
"""

import matplotlib.pyplot as plt

# Mengelompokkan data berdasarkan weather_condition
weather_rentals = hour_df.groupby("weather_condition")["total_rentals"].sum()

# Membuat diagram batang vertikal
plt.figure(figsize=(8, 6))
weather_rentals.plot(kind='bar', color='skyblue')

# Menambahkan judul dan label
plt.title('Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca', fontsize=14)
plt.xlabel('Kondisi Cuaca', fontsize=12)
plt.ylabel('Total Penyewaan Sepeda', fontsize=12)

# Menambahkan jumlah penyewaan di atas batang
for i, value in enumerate(weather_rentals):
    plt.text(i, value + 20000, str(value), ha='center', va='bottom', fontweight='bold', color='black')

# Memutar label pada sumbu X agar lebih mudah dibaca
plt.xticks(rotation=45, ha='right')

# Menampilkan diagram
plt.tight_layout()
plt.show()

"""**Insight:**
Dari data yang ada, dapat disimpulkan bahwa kondisi cuaca jelas mempengaruhi jumlah penyewaan sepeda. Kondisi cuaca Clear (cerah) mencatatkan jumlah penyewaan tertinggi dengan 2,338,173 penyewaan, menunjukkan bahwa cuaca cerah mendorong lebih banyak orang untuk menggunakan sepeda. Sebaliknya, kondisi cuaca Heavy_rainsnow (hujan lebat dan salju) memiliki jumlah penyewaan yang sangat rendah, hanya 223 penyewaan, yang menunjukkan bahwa cuaca buruk mengurangi minat orang untuk menyewa sepeda. Cuaca cerah cenderung meningkatkan aktivitas penyewaan, sementara kondisi cuaca buruk menurunkan jumlah penyewaan sepeda.

## Analisis Lanjutan : Clustering manual berdasarkan jam untuk menjawab pertanyaan 2
Mengubah jam ke dalam interval waktu dalam sehari dengan aturan:
- Dini Hari: 00:00 - 04:59
- Pagi: 05:00 - 10:59
- Siang: 11:00 - 14:59
- Sore: 15:00 - 17:59
- Malam: 18:00 - 23:59
"""

import pandas as pd
import matplotlib.pyplot as plt

# Menggunakan data yang sudah dikelompokkan berdasarkan jam
hourly_rentals = hour_df.groupby("hour")["total_rentals"].sum().sort_values(ascending=False)

# Mengelompokkan data penyewaan sepeda per jam ke dalam kategori waktu
def get_time_of_day(hour):
    if 5 <= hour < 11:
        return 'Pagi'
    elif 11 <= hour < 15:
        return 'Siang'
    elif 15 <= hour < 18:
        return 'Sore'
    elif 18 <= hour < 24:
        return 'Malam'
    else:
        return 'Dini Hari'

# Mengubah data hourly_rentals menjadi DataFrame untuk manipulasi lebih lanjut
hour_df = pd.DataFrame({'hour': hourly_rentals.index, 'total_rentals': hourly_rentals.values})

# Menambahkan kolom 'time_of_day' berdasarkan jam
hour_df['time_of_day'] = hour_df['hour'].apply(get_time_of_day)

# Mengelompokkan data berdasarkan 'time_of_day' dan menjumlahkan total penyewaan sepeda
time_of_day_rentals = hour_df.groupby('time_of_day')['total_rentals'].sum()

# Urutkan dari tertinggi ke terendah
time_of_day_rentals = time_of_day_rentals.sort_values(ascending=False)

print(time_of_day_rentals)

# Visualisasi
ax = time_of_day_rentals.plot(kind='bar', color='skyblue', figsize=(10,6))
plt.title('Penyewaan Sepeda Berdasarkan Waktu dalam Sehari')
plt.xlabel('Waktu dalam Sehari')
plt.ylabel('Total Penyewaan Sepeda')
plt.xticks(rotation=0)

# Menambahkan label di atas batang
for i, v in enumerate(time_of_day_rentals):
    ax.text(i, v + 5000, str(v), ha='center', va='bottom', fontsize=10)

plt.show()

"""**Insight:**
Berdasarkan data di atas, penyewaan sepeda tertinggi terjadi pada jam Malam dengan total 986.109 penyewaan, yang kemungkinan besar terkait dengan aktivitas malam hari, seperti pulang kerja atau rekreasi malam. Sebaliknya, Dini Hari mencatatkan penyewaan sepeda terendah dengan hanya 92.248 penyewaan, yang wajar mengingat pada jam tersebut aktivitas sepeda sangat minim. Secara keseluruhan, penyewaan sepeda cenderung tinggi pada sore hingga malam hari, sementara rendah pada dini hari.

## Conclusion

Berdasarkan analisis data penyewaan sepeda, diperoleh beberapa insight penting yang dapat menjadi dasar pengambilan keputusan untuk optimasi layanan penyewaan sepeda:

1. Penyewaan Sepeda Berdasarkan Hari
   Penyewaan sepeda tertinggi tercatat pada hari Jumat dengan total 487.790 penyewaan, sedangkan penyewaan terendah terjadi pada hari Minggu dengan 444.027 penyewaan.
   - Insight:
     - Tingginya angka penyewaan di hari kerja, khususnya Jumat, kemungkinan besar dipengaruhi oleh aktivitas komuter yang menggunakan sepeda sebagai transportasi menuju kantor atau kampus.
     - Sebaliknya, rendahnya angka di hari Minggu dapat disebabkan oleh menurunnya aktivitas masyarakat dan lebih banyaknya waktu istirahat di akhir pekan.
   - Rekomendasi:
         - Fokuskan distribusi dan perawatan unit sepeda di hari kerja, terutama menjelang akhir minggu.
         - Manfaatkan hari Minggu untuk melakukan pemeliharaan berkala terhadap sepeda-sepeda.
     
2. Penyewaan Sepeda Berdasarkan Jam
   Puncak penyewaan terjadi pada pukul 17:00 dengan 336.860 penyewaan, dan paling rendah pada pukul 04:00 dengan hanya 4.428 penyewaan.

   - Insight:
     - Jam 17:00 merupakan jam pulang kerja/sekolah, menunjukkan bahwa sepeda banyak digunakan sebagai moda transportasi utama saat jam sibuk.
     - Aktivitas penyewaan yang sangat rendah pada pukul 04:00 dapat dikaitkan dengan waktu subuh di mana sebagian besar orang belum memulai aktivitas.
   - Rekomendasi:
     - Tambahkan ketersediaan sepeda di lokasi strategis (seperti stasiun atau perkantoran) menjelang jam sibuk (pagi dan sore hari).
     - Lakukan pemeliharaan sepeda di dini hari ketika tidak banyak peminjaman sepeda
       
3. Penyewaan Sepeda Berdasarkan Bulan
   Bulan Agustus mencatatkan penyewaan tertinggi dengan 351.194 penyewaan, sedangkan Januari adalah yang terendah dengan 134.933 penyewaan.

   - Insight:
     - Musim panas seperti di bulan Agustus cenderung mendukung aktivitas luar ruangan, termasuk bersepeda.
     - Cuaca yang lebih dingin dan curah hujan yang tinggi pada bulan Januari dapat menurunkan minat masyarakat untuk bersepeda.
   - Rekomendasi:
     - Lakukan kampanye promosi penyewaan saat musim panas.
     - Tawarkan insentif atau promo musiman untuk mendorong penyewaan di musim dingin.

4. Penyewaan Sepeda Berdasarkan Kondisi Cuaca
   Kondisi cuaca cerah (Clear) memiliki total penyewaan tertinggi sebesar 2.338.173 penyewaan, sedangkan hujan lebat dan salju (Heavy_rainsnow) hanya mencatatkan 223 penyewaan.
   - Insight:
     - Cuaca sangat mempengaruhi minat pengguna dalam menyewa sepeda. Pada cuaca ekstrem, penyewaan hampir berhenti sepenuhnya.
     - Penggunaan sepeda lebih diminati saat cuaca mendukung.
   - Rekomendasi:
     - Kembangkan sistem informasi cuaca pada aplikasi penyewaan untuk memberikan rekomendasi waktu terbaik bersepeda.
     - Sediakan layanan perlindungan tambahan (seperti jas hujan atau pelindung) saat cuaca tidak menentu.

Data menunjukkan bahwa waktu, musim, dan cuaca memainkan peran penting dalam perilaku penyewaan sepeda. Dengan memahami pola-pola ini, penyedia layanan dapat meningkatkan pengalaman pengguna, mengoptimalkan distribusi sepeda, dan merancang strategi pemasaran yang lebih efektif. Insight ini juga dapat berguna untuk pengembangan kebijakan transportasi ramah lingkungan di kota.
"""