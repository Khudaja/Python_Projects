# 📚 Personal Library Manager

A simple and elegant **Streamlit** app to manage your personal book collection. You can add, edit, delete, search, and export books — all stored locally in a JSON file.

---

## 🚀 Features

- 🔍 **Search Books** by title or author  
- ➕ **Add New Books** with details like author, genre, year, and read status  
- ✏️ **Edit Existing Books** easily  
- ❌ **Delete Books** from your library  
- 📄 **Export your Library** to CSV  
- 💾 All data is saved locally in `library.json`

---

## 🧰 Built With

- **Python**  
- **Streamlit**  
- **Pandas**  
- **FPDF** (optional for PDF export)  
- **JSON** (for data storage)

---

## 💻 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/personal-library-manager.git
cd personal-library-manager

## Install Dependencies
bash
Copy
Edit
pip install streamlit pandas fpdf

## Run the App
bash
Copy
Edit
streamlit run yourfilename.py
```

## File Structure
bash
Copy
Edit
personal-library-manager/
│
├── library.json        # Stores book data locally
├── main.py             # Main Streamlit app file
├── README.md           # This file

## Export Options
Download your full library as a CSV file

(Optional) Extend support for PDF or Excel in future versions

## 🛡️ Data Note

Your data is stored locally in library.json. No cloud or external storage is used.

## 📄 License
This project is licensed under the MIT License.

## 🔗 Links
GitHub Repo: [(https://github.com/Khudaja/Python_Projects/tree/main/personal-library-manager)]

Live App: [Your Streamlit Share Link]](https://pythonprojects-khudaja.streamlit.app/)
