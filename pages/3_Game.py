import streamlit as st

st.title("Game Kriptografi")

#pengertian kripto
with st.container() :
    st.header("Kriptografi")
    st.write("Kriptologi adalah ilmu membuat dan memecahkan kode rahasia. Kriptografi adalah cara untuk menyimpan dan mengirimkan data sehingga hanya penerima yang dituju yang dapat membaca atau memprosesnya. Kriptografi modern menggunakan algoritma yang aman secara komputasi untuk memastikan bahwa penjahat cyber tidak dapat dengan mudah membahayakan informasi yang dilindungi.")
    st.write("Disini kita akan bermain game dengan algoritma kriptografi sederhana seperti _substitution_ dan _transposition_. Yuk main!")

#game
with st.container() :
    st.subheader("1. PZAIZ")
    with st.expander("Clue") :
        st.write("Menggunakan _transposition_ : _Rail Fence Cipher_.")
    tsatu = st.text_input("Jawabanmu", key="satu")
    bsatu = st.button("OK", key="ok1")
    if st.session_state.get('button') != True :
        st.session_state['button'] = bsatu
    if st.session_state['button'] == True :
        if tsatu == "PIZZA" or tsatu == "pizza":
            st.write("**BENAR!** Ini menggunakan _transposition_ : _Rail Fence Cipher_.")
        else :
            st.write("Yah, salah. Ulang lagi ya!")

    st.subheader("2. XBZVASB")
    with st.expander("Clue") :
        st.write("Menggunakan _substitution_ : ROT13 _Cipher_.")
    tdua = st.text_input("Jawabanmu", key="dua")
    bdua = st.button("OK", key="ok2")
    if st.session_state.get('button2') != True :
        st.session_state['button2'] = bdua
    if st.session_state['button2'] == True :
        if tdua == "KOMINFO" or tdua == "kominfo":
            st.write("**BENAR!** Ini menggunakan _substitution_ : ROT13 _Cipher_.")
        else :
            st.write("Yah, salah. Ulang lagi ya!")

    st.subheader("3. CCYUBREIRTSYE")
    with st.expander("Clue") :
        st.write("Menggunakan _transposition_ : _Scytale_.")
    ttiga = st.text_input("Jawabanmu", key="tiga")
    btiga = st.button("OK", key="ok3")
    if st.session_state.get('button3') != True :
        st.session_state['button3'] = btiga
    if st.session_state['button3'] == True :
        if ttiga == "CYBERSECURITY" or ttiga == "cybersecurity":
            st.write("**BENAR!** Ini menggunakan _transposition_ : _Scytale_.")
        else :
            st.write("Yah, salah. Ulang lagi ya!")

    st.subheader("4. SBWKRQ")
    with st.expander("Clue") :
        st.write("Menggunakan _substitution_ : _Caesar Chiper_.")
    tempat = st.text_input("Jawabanmu", key="empat")
    bempat = st.button("OK", key="ok4")
    if st.session_state.get('button4') != True :
        st.session_state['button4'] = bempat
    if st.session_state['button4'] == True :
        if tempat == "PYTHON" or tempat == "python":
            st.write("**BENAR!** Ini menggunakan _substitution_ : _Caesar Chiper_ (+3).")
        else :
            st.write("Yah, salah. Ulang lagi ya!")   