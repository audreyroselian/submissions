import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
mergebike_df = pd.read_csv('mergebike.csv')

st.title(':sparkles: PROYEK ANALISIS DATA :sparkles:')
st.header('Bike Sharing Dataset')


st.subheader("Data")
st.write(mergebike_df)

# Menampilkan deskripsi data
st.subheader("Deskripsi Data")
st.write(mergebike_df.describe(include="all"))

# Pilihan pertanyaan bisnis
option = st.selectbox(
    '## **Pilih Pertanyaan Bisnis:**',
    ('Hubungan Kondisi Cuaca dengan Jumlah Penyewaan', 
     'Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur',
     'Musim Mana yang Meningkatkan Penyewaan Sepeda', 
     'Perbedaan Pola Penyewaan Sepeda berdasarkan Musim dan Hari Kerja')
)

# Menampilkan visualisasi data berdasarkan pilihan pertanyaan
st.subheader("Visualisasi Data")

if option == 'Hubungan Kondisi Cuaca dengan Jumlah Penyewaan':
    # Visualisasi untuk pertanyaan 1
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=mergebike_df, x='cnt_hour', y='weathersit_hour', hue='weathersit_hour', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda per Jam berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Jumlah Penyewaan Sepeda per Jam')
    ax.set_ylabel('Kondisi Cuaca')
    ax.legend(title='Kondisi Cuaca')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=mergebike_df, x='cnt_day', y='weathersit_day', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda per Hari berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Jumlah Penyewaan Sepeda per Hari')
    ax.set_ylabel('Kondisi Cuaca')
    st.pyplot(fig)

elif option == 'Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur':
    # Visualisasi untuk pertanyaan 2
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=mergebike_df, x='workingday_day', y='cnt_day', ax=ax)
    ax.set_title('Perbandingan Jumlah Penyewaan Sepeda antara Hari Kerja dan Akhir Pekan')
    ax.set_xlabel('Hari')
    ax.set_ylabel('Jumlah Penyewaan Sepeda per Hari')
    ax.set_xticks(ticks=[1, 0])
    ax.set_xticklabels(labels=['Hari Kerja', 'Akhir Pekan'])
    st.pyplot(fig)

elif option == 'Musim Mana yang Meningkatkan Penyewaan Sepeda':
    # Visualisasi untuk pertanyaan 3
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=mergebike_df, x='cnt_day', y='season_day', ax=ax)
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
    ax.set_xlabel('Jumlah Penyewaan Sepeda')
    ax.set_ylabel('Musim')
    st.pyplot(fig)

elif option == 'Perbedaan Pola Penyewaan Sepeda berdasarkan Musim dan Hari Kerja':
    # Visualisasi untuk pertanyaan 4
    fig, ax = plt.subplots(figsize=(18, 12))
    sns.barplot(data=mergebike_df, x='season_day', y='cnt_day', hue='workingday_day', palette='coolwarm', ax=ax)
    ax.set_title('Pola Jumlah Penyewaan Sepeda Berdasarkan Musim dan Hari Kerja')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Penyewaan Sepeda per Hari')
    ax.set_xticklabels(labels=ax.get_xticklabels(), rotation=45)
    ax.legend(title='Hari Kerja', loc='upper right')
    st.pyplot(fig)

# Menampilkan kesimpulan
st.subheader("Kesimpulan")

if option == 'Hubungan Kondisi Cuaca dengan Jumlah Penyewaan':
    st.markdown("""
    **Kesimpulan pertanyaan 1** Bagaimana hubungan antara kondisi cuaca dalam per hari dan per jam dengan jumlah penyewaan sepeda?

    Kondisi cuaca dalam per hari dan per jam berhubungan erat dengan jumlah penyewaan sepeda. Jumlah penyewaan sepeda terbanyak terjadi pada saat cuaca cerah (Clear, Few clouds, Partly cloudy, Partly cloudy). Hal ini mengindikasikan kondisi cuaca berkaitan erat dengan jumlah penyewaan. Apabila cuaca buruk, jumlah dalam hitungan jam maupun hari, jumlah penyewaan sepeda pun menurun. Aktivitas luar ruangan seringkali memanfaatkan sepeda dalam keadaan cuaca cerah sehingga tidak terganggu oleh cuaca yang tidak bersahabat.
    """)

elif option == 'Perbedaan Penggunaan Sepeda antara Hari Kerja dan Hari Libur':
    st.markdown("""
    **Kesimpulan pertanyaan 2** Bagaimana perbedaan dalam pola penggunaan sepeda antara hari kerja dan akhir pekan?

    Perbedaan dalam pola penggunaan sepeda antara hari kerja dan hari libur terlihat signifikan. Jumlah penyewa sepeda lebih banyak ketika hari kerja daripada hari libur. Hal ini dapat disebabkan oleh para pekerja lebih nyaman berangkat kerja dengan menggunakan sepeda. Hari kerja juga menjadi hari aktif semua orang sehingga tidak dipungkiri jika penyewaan sepeda lebih ramai di hari kerja. Uji statistik dengan nilai p-value lebih kecil t-statistik mengartikan adanya penolakan hipotesis nol (tidak ada perbedaan antara jumlah penyewaan sepeda pada hari kerja dan akhir pekan). Dengan demikian, kesimpulannya terdapat perbedaan signifikan antara jumlah penyewaan sepeda pada hari kerja dengan hari libur.
    """)

elif option == 'Musim Mana yang Meningkatkan Penyewaan Sepeda':
    st.markdown("""
    **Kesimpulan pertanyaan 3** Pada musim apa penyewaan sepeda meningkat signifikan?

    Jumlah penyewaan sepeda meningkat dengan signifikan pada musim gugur (Fall). Pada musim gugur (Fall) cuaca menjadi cerah sehingga memungkinkan peningkatan signifikan pada penyewaan sepeda.
    """)

elif option == 'Perbedaan Pola Penyewaan Sepeda berdasarkan Musim dan Hari Kerja':
    st.markdown("""
    **Kesimpulan pertanyaan 4** Bagaimana pola jumlah penyewaan sepeda berbeda-beda berdasarkan musim dan hari kerja?

    Jika dilihat berdasarkan musim dan hari kerja, pada musim gugur jumlah penyewaan sepeda pada hari kerja tinggi. Namun, saat musim panas jumlah penyewaan saat hari libur (tidak bekerja) lebih banyak dibandingkan dengan hari kerja saat musim panas. Sebaliknya, saat musim dingin jumlah penyewaan sepeda lebih tinggi pada hari kerja dibandingkan dengan hari libur. Peningkatan jumlah penyewaan sepeda pada musim tertentu bisa jadi disebabkan oleh faktor alam seperti jalanan bersalju menyebabkan kendaraan tidak dapat berjalan dengan normal sehingga banyak yang memilih penyewaan sepeda pada hari kerja, cuaca cerah pada musim tertentu, dan liburan musim panas.
    """)


