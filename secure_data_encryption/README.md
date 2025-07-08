# 🔐 Secure Data Encryption App

A user-friendly Streamlit web app to **encrypt**, **store**, and **retrieve** sensitive data securely using **Fernet encryption** and **SQLite**.

## 📌 Features

- 📝 Store secrets with a unique label and a passkey
- 🔐 Fernet-based encryption and decryption
- 🔑 SHA256 hashing for passkey verification
- 📁 SQLite for local secure storage
- 💡 Clean, responsive UI using Streamlit

---

## 🚀 Getting Started

### 🔧 Prerequisites

Make sure you have Python installed (3.8+ recommended).

Install the required packages:

```bash
pip install streamlit cryptography

```To Run the app
streamlit run main.py

## Project Structure
secure_data_encryption/
│
├── main.py            # Main Streamlit application
├── simple_secret.key  # Fernet encryption key (auto-generated)
├── simple_data.db     # SQLite database (auto-generated)
├── README.md          # Project documentation
