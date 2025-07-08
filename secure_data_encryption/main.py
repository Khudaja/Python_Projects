import streamlit as st
import sqlite3 # use to secure data
import hashlib # passcode ko hashilbe bnay ga
import os
from cryptography.fernet import Fernet #build in encryption sys that encrypt nad decrypt the text

KEY_FILE = "simple_secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write (key) #generate key in binary format 
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return key

cipher = Fernet(load_key())

def init_db ():
    conn = sqlite3.connect("simple_data.db")
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS vault (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        label TEXT,
        encrypted_text TEXT,
        passkey TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest() #secure hash algorithm 256 indicates version. it goona conert a text or code into 64 digit hash

def encrypt (text):
    return cipher.encrypt(text.encode()).decode()

def decrypt(encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()

st.title('😶‍🌫️Secure Data Encryyption App')
menu = ["Store Secret", "Retrieve Secret"]
choice = st.sidebar.selectbox("Choose Option", menu)

if choice == "Store Secret":
    st.markdown("## 🛡️ Store a New Secret")
    st.info("Securely save your private note, password, or token with encryption.")

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            label = st.text_input("🏷️ Label (Unique ID)", key="store_label")
        with col2:
            passkey = st.text_input("🔑 Passkey (used to protect it)", type="password", key="store_passkey")

        st.markdown("### ✍️ Enter Your Secret Below")
        secret = st.text_area("🔒 Your Secret", height=150, key="store_secret")

    if st.button("💾 Encrypt & Save", use_container_width=True):
        if label and secret and passkey:
            conn = sqlite3.connect('simple_data.db')
            c = conn.cursor()

            encrypted = encrypt(secret)
            hashed_key = hash_passkey(passkey)

            try:
                c.execute('INSERT INTO vault (label, encrypted_text, passkey) VALUES (?, ?, ?)',
                          (label, encrypted, hashed_key))
                conn.commit()
                st.success("✅ Secret Saved Successfully!")
            except sqlite3.IntegrityError:
                st.error("⚠️ This label already exists. Use a different one.")
            conn.close()
        else:
            st.warning("❗ Please fill in all the fields.")

elif choice == "Retrieve Secret":
    st.markdown("## 🔍 Retrieve Your Secret")
    st.info("Enter the label and passkey you used to save your secret.")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            label = st.text_input("🔖 Label (case-sensitive):", key="retrieve_label")
        with col2:
            passkey = st.text_input("🔑 Passkey:", type="password", key="retrieve_pass")

    if st.button("🔓 Decrypt Now", use_container_width=True):
        if not label or not passkey:
            st.warning("Please fill in both the Label and Passkey.")
        else:
            conn = sqlite3.connect('simple_data.db')
            c = conn.cursor()
            c.execute('SELECT encrypted_text, passkey FROM vault WHERE label = ?', (label,))
            result = c.fetchone()
            conn.close()

            if result:
                encrypted_text, stored_hash = result
                if hash_passkey(passkey) == stored_hash:
                    try:
                        decrypted = decrypt(encrypted_text)

                        st.success("✅ Secret Decrypted Successfully!")
                        st.markdown("### 🔐 Your Decrypted Secret:")
                        st.code(decrypted, language="text")
                    except Exception as e:
                        st.error(f"Decryption failed: {e}")
                else:
                    st.error("❌ Incorrect Passkey. Please try again.")
            else:
                st.warning("⚠️ No such label found in database.")

             