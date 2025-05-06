import streamlit as st

# Judul aplikasi
st.title("Kalkulator Sederhana")

# Input angka pertama
num1 = st.number_input("Masukkan angka pertama", format="%.2f")

# Input angka kedua
num2 = st.number_input("Masukkan angka kedua", format="%.2f")

# Pilih operasi
operation = st.selectbox("Pilih operasi", ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"])

# Tombol untuk menghitung
if st.button("Hitung"):
    if operation == "Penjumlahan":
        result = num1 + num2
        st.success(f"Hasil penjumlahan: {result:.2f}")
    elif operation == "Pengurangan":
        result = num1 - num2
        st.success(f"Hasil pengurangan: {result:.2f}")
    elif operation == "Perkalian":
        result = num1 * num2
        st.success(f"Hasil perkalian: {result:.2f}")
    elif operation == "Pembagian":
        if num2 != 0:
            result = num1 / num2
            st.success(f"Hasil pembagian: {result:.2f}")
        else:
            st.error("Tidak bisa membagi dengan nol!")
