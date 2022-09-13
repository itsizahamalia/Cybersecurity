from turtle import color
import streamlit as st
from PIL import Image

st.title("About Us")
left_column, right_column = st.columns(2)
with left_column :
    st.image(Image.open('lainlain/ceriaputih.jpg'), width=300)
with right_column :
    st.write("")
    st.write("")
    st.write("'**Happiness can be found even in the darkest of time, when one only remembers to turn on the light.**' - Albus Dumbledore")
    st.write("Kami memilih nama Ceria sebagai nama tim kami karena kami ingin memberi keceriaan dan kebahagiaan bagi semua orang. Kami ingin menyalakan lampu kreatifitas untuk kehidupan yang lebih baik.")
st.subheader("Members")
izah, afika, elfira = st.columns(3)
with izah :
    st.image(Image.open('lainlain/izah.jpg'))
    st.write("**Izah Amalia** \n\n Matematika - Institut Teknologi Sepuluh Nopember \n\n Karyawan Swasta")
    st.write("[LinkedIn Izah](http://tiny.cc/LinkedInIzah)")
with afika :
    st.image(Image.open('lainlain/afika.jpg'))
    st.write("**Nur Afika** \n\n Ilmu Kelautan - Universitas Hasanuddin \n\n Mahasiswa")
    st.write("[LinkedIn Afika](https://www.linkedin.com/in/nurafika-ys)")
with elfira :
    st.image(Image.open('lainlain/elfira.jpg'))
    st.write("**Elfira Ratna Syaharani** \n\n Sains Data - Universitas Pembangunan Nasional 'Veteran' Jawa Timur \n\n Mahasiswa")
    st.write("[LinkedIn Elfira](https://www.linkedin.com/in/elfira-ratna-sy-7a0334216)")