import streamlit as st
import json
import os
import pandas as pd
from io import BytesIO

# Load and save library data
def load_library():
    if not os.path.exists("library.json") or os.path.getsize("library.json") == 0:
        with open("library.json", "w") as file:
            json.dump([], file)

    with open("library.json", "r") as file:
        return json.load(file)

def save_library():  # 💡 You forgot to define this function
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("Select an option", ["View Library", "Add Book", "Edit Book", "Delete Book", "Search Book", "Save & Exit", "Export Library"])  # 💡 Typo fixed: "Veiw" → "View"

# View Library
if menu == "View Library":
    st.sidebar.header("📚 Your Library")

    if library:
        for book in library:
            with st.expander(f"📘 {book['title']} ({book['year']})"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Author:** {book['author']}")
                    st.markdown(f"**Genre:** {book['genre']}")
                with col2:
                    status = "✅ Read" if book['read_status'] else "📖 Not Read"
                    st.markdown(f"**Status:** {status}")
    else:
        st.info("📭 Your Library is Empty.")

# Add Book
elif menu == "Add Book":
    st.sidebar.header("➕ Add a New Book")

    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input("📖 Book Title")
        year = st.number_input("📅 Year", min_value=2022, max_value=2100, step=1)

    with col2:
        author = st.text_input("✍️ Author")
        genre = st.text_input("🏷️ Genre")

    read_status = st.checkbox("✅ Mark as Read")

    st.markdown("---")
    if st.button("📚 Add Book", use_container_width=True):
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        }
        library.append(new_book)
        save_library()
        st.success("✅ Book Added to Your Library!")
        st.rerun()


# Edit Book
elif menu == "Edit Book":
    st.sidebar.header("✏️ Edit a Book")

    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book_title = st.selectbox("📘 Select a Book to Edit", book_titles)
        book_to_edit = next((book for book in library if book["title"] == selected_book_title), None)

        if book_to_edit:
            st.markdown(f"### ✍️ Editing: `{book_to_edit['title']}`")

            col1, col2 = st.columns(2)

            with col1:
                new_title = st.text_input("📖 Title", value=book_to_edit["title"])
                new_year = st.number_input("📅 Year", min_value=2022, max_value=2100, step=1, value=book_to_edit["year"])

            with col2:
                new_author = st.text_input("✍️ Author", value=book_to_edit["author"])
                new_genre = st.text_input("🏷️ Genre", value=book_to_edit["genre"])

            new_read_status = st.checkbox("✅ Mark as Read", value=book_to_edit["read_status"])

            st.markdown("---")

            if st.button("💾 Update Book", use_container_width=True):
                updated_book = {
                    "title": new_title,
                    "author": new_author,
                    "year": new_year,
                    "genre": new_genre,
                    "read_status": new_read_status
                }

                index = library.index(book_to_edit)
                library[index] = updated_book
                save_library()
                st.success("✅ Book Updated Successfully!")
                st.rerun()
    else:
        st.info("📭 No books available to edit.")

# Delete Book
elif menu == "Delete Book":
    st.sidebar.header("Delete a Book")  # 💡 Fixed: st.sidebar("text") → st.sidebar.header("text")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a Book to Delete", book_titles)
        if st.button("Delete Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("Book Deleted From Your Library")
            st.rerun()
    else:
        st.write("No Books to Delete. Please Add a Book")

# Search Book
elif menu == "Search Book":
    st.sidebar.header("🔎 Search a Book")

    search_query = st.text_input("🔤 Enter Book Title or Author")

    if st.button("🔍 Search", use_container_width=True):
        search_results = [
            book for book in library
            if search_query.lower() in book["title"].lower()
            or search_query.lower() in book["author"].lower()
        ]

        if search_results:
            st.markdown(f"### 🔎 Search Results for: `{search_query}`")
            for book in search_results:
                with st.expander(f"📘 {book['title']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Author:** {book['author']}")
                        st.markdown(f"**Genre:** {book['genre']}")
                    with col2:
                        st.markdown(f"**Year:** {book['year']}")
                        st.markdown(f"**Status:** {'✅ Read' if book['read_status'] else '📖 Not Read'}")
        else:
            st.warning("🚫 No Books Found")


# Save & Exit
elif menu == "Save & Exit":
    save_library()
    st.success("Library Saved")

#Export Library
elif menu == "Export Library":
    st.sidebar.header("📤 Export Library")

    if not library:
        st.warning("📭 Your Library is empty. Add books to export.")
    else:
        df = pd.DataFrame(library)

        # Show as Table
        st.dataframe(df)

        # CSV Export
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📄 Download as CSV",
            data=csv,
            file_name='library.csv',
            mime='text/csv',
            use_container_width=True
        )
