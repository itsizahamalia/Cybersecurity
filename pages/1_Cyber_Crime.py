import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

#lottie
def load_lottieurl(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

st.title("Cyber Crime dan Macam-Macamnya")

#pengertian cyber crime
with st.container() :
    st.expander("ddd")
    st.header("Cyber Crime")
    st_lottie(load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_x1ikbkcj.json"), height=300)
    st.write("Cyber crime atau serangan siber adalah segala bentuk kejahatan yang terjadi di dunia maya. Dikutip dari buku _Pengantar Teknologi dan Informasi (2020)_ karya Dasril Aldo dkk, _cyber crime_ adalah kejahatan yang ditimbulkan karena pemanfaatan teknologi internet. Kejahatan ini melibatkan komputer, jaringan dan perangkat yang terhubung dalam jaringan. Pelaku kejahatan siber menargetkan data pribadi atau perusahaan untuk dicuri dan dijual kembali.")

#macam-macam
with st.container() :
    st.write("##")
    st.header("Macam-Macam Cyber Crime")
    st.write("Di jaman serba modern ini, ancaman _cyber crime_ sudah berkembang pesat menjadi berbagai macam. Beberapa macam _cyber crime_ akan dibahas di halaman ini.")

#phishing    
    st.subheader("1. Phishing")
    st.write("Phishing adalah suatu tindakan penipuan agar seseorang memberikan data ataupun informasi pribadinya. Umumnya aksi kejahatan ini dilancarkan melalui email maupun media sosial lain, seperti mengirimi _link_ palsu, membuat _website_ bodong, dan sebagainya untuk mencuri data penting korban, seperti _password_, PIN, OTP, dan lain-lain.")
#cracking    
    st.subheader("2. Cracking")
    st.write("_Cracking_ adalah percobaan memasuki sistem komputer secara paksa dengan meretas sistem keamanan _software_ atau komputer untuk tujuan ilegal yang mengarah ke kriminalisme. Pelaku _cracking_ melakukan aksinya untuk mencuri, melihat, memanipulasi data hingga penanaman _malware_.")
#injeksi SQL
    st.subheader("3. Injeksi SQL")
    st.write("Injeksi SQL atau _Structured Query Language_ adalah sebuah tipe ancaman yang dilancarkan untuk mengambil alih sekaligus mencuri data dari suatu jaringan pusat. Melalui SQL, pelaku kejahatan memanfaatkan celah pada aplikasi guna menyisipkan kode berbahaya ke dalam database.")
#ransomware
    st.subheader("4. Serangan Ransomware")
    st.write("Ransomware adalah tipe _malware_ yang menargetkan perangkat keras untuk mengambil informasi berharga dari targetnya kemudian mengenkripsi dan mengunci file tersebut. Jika ingin membuka atau mengakses kembali data-data tersebut, pelaku akan meminta uang tebusan ke korban. Apabila korban tidak mengabulkan permintaan tersebut, pelaku tak segan mengancam akan membuat data tidak bisa digunakan lagi.")
#DDoS
    st.subheader("5. Serangan DDoS")
    st.write("_Distributed Denial of Service_ (DDoS) adalah contoh _cyber crime_ dengan membuat lalu lintas server berjalan dengan beban berat hingga tidak bisa menampung koneksi dari user lain/_overload_. Serangan yang populer dilakukan oleh hacker ini dibuat dengan cara mengirimkan request ke server secara terus menerus dengan transaksi data yang besar.")

#Source : https://www.jagoanhosting.com/blog/cyber-security-adalah/#:~:text=Salah%20satu%20contoh%20cyber%20security,terjadinya%20kebocoran%20atau%20pencurian%20data.
# https://www.dewaweb.com/blog/pengertian-dan-jenis-cyber-crime/
# https://www.kompas.com/skola/read/2022/04/25/100000169/cyber-crime--definisi-jenis-dan-contohnya?page=all
