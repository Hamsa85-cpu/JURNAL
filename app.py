import streamlit as st

st.set_page_config(
    page_title="Jurnal Guru Premium",
    page_icon="📚",
    layout="wide"
)

if "login" not in st.session_state:
    st.session_state.login = False

st.title("📚 Jurnal Guru Premium")

if not st.session_state.login:

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.login = True
            st.success("Login berhasil")
            st.rerun()
        else:
            st.error("Username atau password salah")

else:
    st.sidebar.success("Login Berhasil")

    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Jurnal", 0)
    col2.metric("Total Kehadiran", 0)
    col3.metric("Total Nilai", 0)

    st.info("Selamat datang di Aplikasi Jurnal Guru Premium")
