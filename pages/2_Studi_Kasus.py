from PIL import Image
import requests
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie

#lottie
def load_lottieurl(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

st.title("Phishing di Dunia Finansial")
tab1, tab2, tab3, tab4 = st.tabs(["Phishing", "Latar Belakang", "Masalah", "Solusi"])

with tab1:
    st.header("Apa Itu Phishing?")
    st_lottie(load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_ewya1ucg.json"), height=300)
    st.write("Phishing adalah tindakan penipuan agar seseorang memberikan data ataupun informasi pribadinya. Pelaku kejahatan ini dikenal dengan sebutan Phisher. Mereka berupaya untuk mendapatkan informasi pribadi seperti nama pengguna, password, hingga informasi kartu kredit.")
    st.subheader("Contoh Email Phishing")
    left_column, right_column = st.columns(2)
    with left_column :
        st.image(Image.open('lainlain/email phishing4.jpg'))
    with right_column :
        st.image(Image.open('lainlain/email phishing2.png'))
    st.write("Selain email phishing, akhir-akhir ini marak terjadi phishing dalam bentuk chat WhatsApp yang mengaku sebagai Bank BRI. Dalam chat tersebut dilampirkan pengumuman yang menyatakan bahwa tarif transfer antar bank naik menjadi Rp.150.000 per bulan untuk unlimited transaksi. Penerima chat diminta untuk membalas chat dan mengisi form bila tidak setuju.")
    left_column, right_column = st.columns(2)
    with left_column :
        st.image(Image.open('lainlain/bri phishing2.jpg'))
    with right_column :
        st.image(Image.open('lainlain/bri phishing.jpg'))


with tab2:
    st.header("Latar Belakang Masalah")
    st.write("Indonesia Anti-Phishing Data Exchange (IDADX) mencatat jumlah phishing yang terjadi di Indonesia per kuartal di tahun 2022 ini. Di kuartal kedua tahun ini, total ada 8.759 kasus phishing yang terjadi di Indonesia.")
    phishing = st.selectbox("Pilih Kuartal : ", ('Kuartal I (Januari - Maret)', 'Kuartal II (April - Juni)'))
    if phishing == 'Kuartal I (Januari - Maret)' :
        df_phishingkuartal1 = pd.DataFrame({
        'Laporan': [1210, 994, 965],
        'Bulan': ["Januari 2022", "Februari 2022", "Maret 2022"]
        })
        fig = plt.figure()
        plt.bar(df_phishingkuartal1['Bulan'], df_phishingkuartal1['Laporan'], color='#008B45')
        plt.text(-0.13, 1215, '1.210')
        plt.text(0.9, 999, '994')
        plt.text(1.9, 970, '965')
        plt.ylim(0, 1300)
        plt.xlabel('Tahun', style='italic')
        plt.ylabel('Jumlah Phishing', style='italic')
        plt.title('Jumlah Laporan Phising\n(Kuartal I 2022)\n', fontweight='bold')
        st.pyplot(fig)
        st.caption("Source : Indonesia Anti-Phishing Data Exchange (IDADX)")
        st.write("Pada kuartal pertama tahun ini, kasus phishing paling banyak terjadi pada bulan Januari dengan total 1.210 laporan. Kemudian, kasusnya menurun pada Februari dan Maret menjadi 994 laporan dan 965 laporan. IDADX juga melaporkan jumlah oraganisasi yang diincar serangan phishing sebanyak 58 kasus dan ada 125 nama domain sepanjang Januari-Maret 2022. Menurut catatan IDADX, kuartal pertama tahun 2022 mengalami peningkatan dibanding kuartal pertama tahun 2021 sebanyak 536 kasus phishing.")

        labels = 'Lembaga Keuangan', 'E-commerce & Retail', 'Aset Kripto', 'Media Sosial', 'Internet Service Provider', 'Gaming'
        sizes = [50, 27, 11, 5, 5, 2]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
        plt.title("Sasaran Phishing\n(Kuartal I 2022) \n", fontweight='bold')
        ax1.axis('equal')
        st.pyplot(fig1)
        st.caption("Source : Indonesia Anti-Phishing Data Exchange (IDADX)")
        st.write("Menurut laporan tersebut, lembaga keuangan menjadi sasaran utama serangan dengan mencatat 50% dari total kasus yang terjadi, disusul dengan e-commerce atau retail (27%), aset kripto (11%), media sosial (5%), Internet Service Provider (5%), dan gaming (2%).")
    else :
        df_phishingkuartal2 = pd.DataFrame({
        'Laporan': [2122, 1693, 1764],
        'Bulan': ["April 2022", "Mei 2022", "Juni 2022"]
        })
        fig = plt.figure()
        plt.bar(df_phishingkuartal2['Bulan'], df_phishingkuartal2['Laporan'], color='#008B45')
        plt.text(-0.13, 2132, '2.122')
        plt.text(0.9, 1703, '1.693')
        plt.text(1.9, 1774, '1.764')
        plt.ylim(0, 2300)
        plt.xlabel('Tahun', style='italic')
        plt.ylabel('Jumlah Phishing', style='italic')
        plt.title('Jumlah Laporan Phising\n(Kuartal II 2022)\n', fontweight='bold')
        st.pyplot(fig)
        st.caption("Source : Indonesia Anti-Phishing Data Exchange (IDADX)")
        st.write("Pada kuartal kedua tahun 2022, terjadi peningkatan cukup signifikan menjadi 5.579 kasus phishing. Kasus tertinggi terjadi di bulan April sebanyak 2.122 kasus. Menurut informasi IDADX, kuartal kedua tahun 2022 ini juga mengalami peningkatan dari kuartal kedua tahun 2021 sebanyak 1.637 kasus phishing.")

        labels = 'Lembaga Keuangan', 'E-commerce & Retail', 'Media Sosial', 'Aset Kripto', 'Gaming'
        sizes = [41, 32, 21, 3, 3]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
        plt.title("Sasaran Phishing\n(Kuartal II 2022) \n", fontweight='bold')
        ax1.axis('equal')
        st.pyplot(fig1)
        st.caption("Source : Indonesia Anti-Phishing Data Exchange (IDADX)")
        st.write("Di kuartal kedua, lembaga keuangan masih menjadi sektor yang paling ditargetkan menjadi sasaran phishing walaupun nilainya sudah turun dibanding kuartal pertama, yaitu sebesar 41%. Diikuti oleh E-commerse atau Retail sebesar 32%, Media Sosial sebesar 21%, serta Aset Kripto dan Gaming sebesar 3%.")

with tab3:
    st.header("Studi Kasus")
    st_lottie(load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_znbkacgx.json"), height=300)
    st.write("Dalam sektor finansial, pelaku kejahatan phishing biasanya mengirim email kepada nasabah yang mengharuskan nasabah untuk memperbarui akun pribadinya, dengan ancaman bila tidak diperbarui, maka akun akan diblokir. Nasabah diarahkan untuk masuk ke link alamat resmi milik bank, tetapi pada saat link tersebut diklik, alamat link dibelokkan ke alamat palsu milik pelaku. Sehingga banyak nasabah yang tertipu dan memasukkan username, password, dan nomor pin ke alamat palsu milik pelaku.")
    

with tab4:
    st.header("Cara Mengatasi Phishing")
    st.subheader("1. Menggunakan Two-Factor Authentication")
    st.write("Two-Factor Authentication adalah verifikasi dua langkah, yaitu password dan ponsel. Pada saat pelaku phising sudah menemukan username dan password tapi tidak dapat memasukan kode verifikasi ponsel, platform tidak akan melanjutkan proses. Sehingga akun akan terlindungi dengan lebih baik.")
    st.subheader("2. Cek Alamat Pengirim Email")
    st.write("Jenis phishing yang masih marak digunakan adalah email phishing. Cek alamat pengirim email setiap mendapatkan email, biasanya instansi besar memiliki domain sendiri. Bila ada email yang mengaku dari instansi besar tetapi memakai domain yang berbeda dengan nama instansi, email tersebut perlu dicurigai. Selain itu, bisa dilakukan double check dengan mencari alamat email tersebut di google.")
    st.subheader("3. Jangan Asal Klik Link")
    st.write("Email dan website phishing biasanya dibuat hampir mirip dengan email dan website aslinya. Sebelum klik website yang diberikan oleh orang atau email yang tidak dikenal, pastikan link tersebut aman dengan cara mengarahkan kursor ke link tersebut tanpa diklik atau hover. Lalu, akan muncul informasi URL dari link tersebut. Jika mengarah ke website asli, berarti link aman. Jika tidak, sebaiknya jangan diklik link tersebut.")
    st.subheader("4. Baca Pesan dengan Seksama")
    st.write("Ketika mendapatkan pesan atau email, baca pesan tersebut dengan seksama. Perhatikan dengan teliti apakah ada kesalahan ketik, penggunaan kata yang tidak sesuai, atau karakter aneh yang ada pada pesan tersebut. Beberapa kesalahan ketik sengaja dibuat untuk melewati filter spam dari pengaturan keamanan.")
    st.subheader("5. Unduh Aplikasi Anti-Malware")
    st.write("Dengan menggunakan aplikasi anti-malware, pengguna dapat melindungi data digital yang dimiliki. Aplikasi anti-malware ini juga akan menjadi pengaman tambahan agar terhindar dari upaya phishing.")

#Source : https://databoks.katadata.co.id/datapublish/2022/06/08/idadx-ada-3180-laporan-phishing-pada-kuartal-i-2022
# https://www.cnnindonesia.com/teknologi/20220325194851-192-776315/3180-serangan-phishing-awal-2022-lembaga-keuangan-jadi-sasaran-utama.
# https://www.niagahoster.co.id/blog/mengatasi-phishing/
# https://www.tek.id/tek/tips-menghindari-serangan-phishing-b2fl39nZR
