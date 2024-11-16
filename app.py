import streamlit as st

# Fungsi untuk menghitung FPB
def fpb(a, b):
    while b:
        a, b = b, a % b
    return a

# Fungsi untuk mengenkripsi teks menggunakan Affine Cipher
def affine_encrypt(plaintext, a, b):
    cipher = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a')
            encrypted_char = (a * shift + b) % 26
            cipher += chr(encrypted_char + ord('a')) if char.islower() else chr(encrypted_char + ord('A'))
        else:
            cipher += char
    return cipher

# Fungsi untuk mendekripsi teks menggunakan Affine Cipher
def affine_decrypt(ciphertext, a, b):
    a_inv = pow(a, -1, 26)  # Invers dari a modulo 26
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char.lower()) - ord('a')
            decrypted_char = a_inv * (shift - b) % 26
            plaintext += chr(decrypted_char + ord('a')) if char.islower() else chr(decrypted_char + ord('A'))
        else:
            plaintext += char
    return plaintext

# Antarmuka pengguna dengan Streamlit
st.title("Affine Cipher Encryptor and Decryptor")
st.write("Encrypt and decrypt text using the Affine Cipher.")

# Input pengguna untuk teks dan kunci
plaintext = st.text_area("Enter Text to Encrypt/Decrypt:")
a = st.number_input("Enter value for 'a' (should be coprime with 26):", min_value=1, max_value=25)
b = st.number_input("Enter value for 'b':", min_value=0, max_value=25)

# Validasi jika 'a' relatif prima dengan 26
if fpb(a, 26) != 1:
    st.error("Value of 'a' must be coprime with 26!")
else:
    # Pilihan untuk mengenkripsi atau mendekripsi
    mode = st.selectbox("Choose operation", ("Encrypt", "Decrypt"))

    if mode == "Encrypt":
        if plaintext:
            encrypted_text = affine_encrypt(plaintext, a, b)
            st.subheader("Encrypted Text")
            st.write(encrypted_text)
    elif mode == "Decrypt":
        if plaintext:
            decrypted_text = affine_decrypt(plaintext, a, b)
            st.subheader("Decrypted Text")
            st.write(decrypted_text)
