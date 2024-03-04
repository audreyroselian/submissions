import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("mergebike.csv")

# Tampilkan judul aplikasi
st.title("Dashboard Data")

# Tampilkan data dalam bentuk tabel
st.write("Data:", data)

# Tampilkan pilihan untuk memilih kolom yang ingin divisualisasikan
column_to_visualize = st.selectbox("Pilih kolom untuk divisualisasikan:", data.columns)

# Visualisasikan data berdasarkan pilihan pengguna
if st.button("Tampilkan Visualisasi"):
    plt.figure(figsize=(10, 6))
    plt.hist(data[column_to_visualize], bins=20)
    plt.xlabel(column_to_visualize)
    plt.ylabel("Frekuensi")
    plt.title("Histogram " + column_to_visualize)
    st.pyplot()

# Tampilkan statistik deskriptif dari data
if st.checkbox("Tampilkan Statistik Deskriptif"):
    st.write("Statistik Deskriptif:")
    st.write(data.describe())

# Tampilkan footer atau informasi tambahan
st.sidebar.text("Informasi Tambahan:")
st.sidebar.write("Proyek Dashboard - Streamlit")
st.sidebar.write("Dibuat oleh [Nama Anda]")
