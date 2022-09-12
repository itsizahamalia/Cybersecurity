import requests
from streamlit_lottie import st_lottie
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import NullFormatter
import logging

#lottie
def load_lottieurl(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

st.title("Cyber Security")
st_lottie(load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_lwcar9tv.json"), height=300)
st.write("Menurut Kaspersky _cyber security_ adalah suatu praktik melindungi para komputer, server, perangkat _mobile_, sistem elektronik, jaringan, dan data dari serangan-serangan jahat. Begitu pula Cisco yang mendefinisikan _cyber security_ sebagai praktik melindungi berbagai sistem, jaringan, dan program dari serangan-serangan digital.")
st.write("Jadi, _cyber security_ atau keamanan siber bisa dibilang merupakan tindakan untuk melindungi informasi di dunia maya dari aneka serangan.")
st.write("Menurut data _National Cyber Security Index_ (NCSI) per tanggal 7 Maret 2022, _cyber security_ atau keamanan Indonesia berada di peringkat ke-6 Asia Tenggara dan peringkat ke-83 dari 160 negara.")
df_indexcybersec = pd.DataFrame({
    'Skor' :[10.39, 15.58, 18.18, 36.36, 38.96, 41.56, 63.64, 64.94, 72.43, 79.22],
    'Negara' : ["Myanmar", "Kamboja", "Laos", "Vietnam", "Indonesia", "Brunei Darussalam", "Filipina", "Thailand", "Singapura", "Malaysia"]
})
fig = plt.figure()
plt.barh(df_indexcybersec['Negara'], df_indexcybersec['Skor'], color='#008B45')
plt.text(10.39, -0.13, "10.39")
plt.text(15.58, 0.88, "15.58")
plt.text(18.18, 1.88, "18.18")
plt.text(36.36, 2.88, "36.36")
plt.text(38.96, 3.88, "38.96")
plt.text(41.56, 4.88, "41.56")
plt.text(63.64, 5.88, "63.64")
plt.text(64.94, 6.88, "64.94")
plt.text(72.43, 7.88, "72.43")
plt.text(79.22, 8.88, "79.22")
plt.xlim(0,90)
plt.xlabel("Skor", style='italic')
plt.title("Indeks Keamanan Siber\nNegara-Negara Asia Tenggara (2022)\n", fontweight='bold')
st.pyplot(fig)
st.caption("Source : National Cyber Security Index, 7 Maret 2022")
st.write("NCSI membuat penilaian ini berdasarkan sejumlah indikator, seperti aturan hukum negara terkait keamanan siber, ada atau tidaknya lembaga pemerintah di bidang keamanan siber, kerja sama pemerintah terkait keamanan siber, serta bukti-bukti publik seperti situs resmi pemerintah atau program lain yang terkait.")
st.write("Dengan indikator tersebut, NCSI menilai Indonesia memiliki skor 38,96 dari 100 dalam hal keamanan siber. Angka itu jauh di bawah skor negara-negara tetangga. Padahal, pengguna internet di Indonesia mencapai 204.7 juta, yang berarti 73% penduduk Indonesia telah menggunakan internet.")

st.write("Hal ini selaras dengan informasi dari Badan Siber dan Sandi Negara (BSSN) mengenai anomali trafik yang terjadi di Indonesia semakin meningkat setiap tahun. Bahkan pada awal tahun 2022 sudah ada 285 juta anomali trafik.")
anomali = st.radio("Pilih tahun : ", ("2020", "2021", "2022 (Januari-Februari)"))
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
if anomali == "2020" :
    logging.basicConfig(level='INFO')
    mlogger = logging.getLogger('matplotlib')
    mlogger.setLevel(logging.WARNING)
    df_traffic = pd.DataFrame({
        'Jumlah' : [25224811, 29188645, 26423989, 18088514, 19323941, 31533717, 40153925, 63054697, 53654789, 66402749, 50194276, 72093149],
        'Tahun' : ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    })
    def formatter(x, pos):
        return str(round(x / 1e6, 1)) + " million"
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    ax.yaxis.set_minor_formatter(NullFormatter())
    plt.plot(df_traffic['Tahun'], df_traffic['Jumlah'], color='#008B45')
    plt.text(0.2, 23000000, "25.224.811", horizontalalignment='center', fontsize=7)
    plt.text(1, 30000000, "29.188.645", horizontalalignment='center', fontsize=7)
    plt.text(2.85, 26000000, "26.423.989", horizontalalignment='center', fontsize=7)
    plt.text(3, 16500000, "18.088.514", horizontalalignment='center', fontsize=7)
    plt.text(4.1, 19323941, "19.323.941", fontsize=7)
    plt.text(3.5, 31533717, "31.533.717", fontsize=7)
    plt.text(6.1, 40153925, "40.153.925", fontsize=7)
    plt.text(6.3, 64000000, "63.054.697", fontsize=7)
    plt.text(7.4, 52000000, "53.654.789", fontsize=7)
    plt.text(8.4, 67000000, "66.402.749", fontsize=7)
    plt.text(9.4, 48500000, "50.194.276", fontsize=7)
    plt.text(10, 73000000, "72.093.149", fontsize=7)
    plt.xlabel("Tahun", style='italic')
    plt.ylabel("Jumlah Anomali", style='italic')
    plt.title("Anomali Trafik Tahun 2020", fontweight='bold')
    st.pyplot(fig)
    st.caption("Source : BSSN")

elif anomali == "2021" :
    logging.basicConfig(level='INFO')
    mlogger = logging.getLogger('matplotlib')
    mlogger.setLevel(logging.WARNING)
    df_traffic = pd.DataFrame({
        'Jumlah' : [59316206, 44901308, 50402748, 115989735, 186202637, 164446175, 120593162, 146950765, 123645909, 186985509, 196563700, 242066168],
        'Tahun' : ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] 
    })
    def formatter(x, pos):
        return str(round(x / 1e6, 1)) + " million"
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    ax.yaxis.set_minor_formatter(NullFormatter())
    plt.plot(df_traffic['Tahun'], df_traffic['Jumlah'], color='#008B45')
    plt.text(-0.4, 62000000, "59.316.206", fontsize=7)
    plt.text(0.4, 38000000, "44.901.308", fontsize=7)
    plt.text(2.1, 49000000, "50.402.748", fontsize=7)
    plt.text(3.1, 115989735, "115.989.735", fontsize=7)
    plt.text(3.2, 190000000, "186.202.637", fontsize=7)
    plt.text(5.1, 164000000, "164.446.175", fontsize=7)
    plt.text(5.3, 112000000, "120.593.162", fontsize=7)
    plt.text(6.3, 150000000, "146.950.765", fontsize=7)
    plt.text(7.3, 117000000, "123.645.909", fontsize=7)
    plt.text(7.4, 185000000, "186.985.509", fontsize=7)
    plt.text(10, 191000000, "196.563.700", fontsize=7)
    plt.text(10, 245000000, "242.066.168", fontsize=7)
    plt.ylim(0,270000000)
    plt.xlabel("Tahun", style='italic')
    plt.ylabel("Jumlah Anomali", style='italic')
    plt.title("Anomali Trafik Tahun 2021", fontweight='bold')
    st.pyplot(fig)
    st.caption("Source : BSSN")

else :
    logging.basicConfig(level='INFO')
    mlogger = logging.getLogger('matplotlib')
    mlogger.setLevel(logging.WARNING)
    df_traffic = pd.DataFrame({
        'Jumlah' : [273313399, 111773819],
        'Tahun' : ["Jan", "Feb"]
    })
    def formatter(x, pos):
        return str(round(x / 1e6, 1)) + " million"
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    ax.yaxis.set_minor_formatter(NullFormatter())
    plt.plot(df_traffic['Tahun'], df_traffic['Jumlah'], color='#008B45')
    plt.text(-0.04, 277000000, "273.313.399", fontsize=7)
    plt.text(0.9, 103000000, "111.773.819", fontsize=7)
    plt.ylim(0,290000000)
    plt.xlabel("Tahun", style='italic')
    plt.ylabel("Jumlah Anomali", style='italic')
    plt.title("Anomali Trafik Tahun 2022\n(Januari-Februari)", fontweight='bold')
    st.pyplot(fig)
    st.caption("Source : BSSN")

st.write("Dari grafik di atas, terlihat dari tahun 2020 ke tahun 2021, jumlah anomali meningkat empat kali lipat. Bila dihubungkan dengan rendahnya skor _cyber security_ di Indonesia menurut NCSI, maka pemerintah dan warga Indonesia perlu meningkatkan kualitas _cyber security_, mengingat jumlah pengguna internet di Indonesia terus meningkat.")


#Source : https://infokomputer.grid.id/read/122710604/apa-itu-cyber-security-mengapa-cyber-security-kini-makin-penting?page=all
#https://www.niagahoster.co.id/blog/cyber-security-adalah/
#https://www.linovhr.com/cyber-security/
#https://www.dewaweb.com/blog/apa-itu-cyber-security/
#https://runsystem.id/id/blog/cyber-security/#