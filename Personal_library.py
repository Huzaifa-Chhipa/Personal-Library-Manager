import streamlit as st

# Initialize the library in session state
if "library" not in st.session_state:
    st.session_state.library = []

def add_book():
    """Add a book to the library."""
    st.subheader("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1800, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Have you read this book?")

    if st.button("Add Book"):
        if title and author and genre:
            book = {
                "title": title,
                "author": author,
                "year": year,
                "genre": genre,
                "read_status": read_status
            }
            st.session_state.library.append(book)
            st.success("Book added successfully!")
        else:
            st.error("Please fill in all fields.")

def remove_book():
    """Remove a book from the library."""
    st.subheader("Remove a Book")
    if st.session_state.library:
        titles = [book["title"] for book in st.session_state.library]
        selected_title = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != selected_title]
            st.success("Book removed successfully!")
    else:
        st.warning("Your library is empty.")

def search_book():
    """Search for a book by title or author."""
    st.subheader("Search for a Book")
    search_option = st.radio("Search by:", ["Title", "Author"])
    search_term = st.text_input(f"Enter the {search_option.lower()}:")

    if search_term:
        if search_option == "Title":
            results = [book for book in st.session_state.library if search_term.lower() in book["title"].lower()]
        else:
            results = [book for book in st.session_state.library if search_term.lower() in book["author"].lower()]

        if results:
            st.write("Matching Books:")
            for book in results:
                status = "Read" if book["read_status"] else "Unread"
                st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            st.warning("No matching books found.")

def display_all_books():
    """Display all books in the library."""
    st.subheader("Your Library")
    if st.session_state.library:
        for i, book in enumerate(st.session_state.library, 1):
            status = "Read" if book["read_status"] else "Unread"
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.warning("Your library is empty.")

def display_statistics():
    """Display library statistics."""
    st.subheader("Library Statistics")
    total_books = len(st.session_state.library)
    read_books = sum(book["read_status"] for book in st.session_state.library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    st.write(f"Total books: {total_books}")
    st.write(f"Percentage read: {percentage_read:.1f}%")

def main():
    """Main function to run the Streamlit app."""
    st.title("Personal Library Manager 📚")

    # Sidebar menu
    st.sidebar.title("Menu")
    options = ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"]
    choice = st.sidebar.radio("Select an option", options)

    if choice == "Add a Book":
        add_book()
    elif choice == "Remove a Book":
        remove_book()
    elif choice == "Search for a Book":
        search_book()
    elif choice == "Display All Books":
        display_all_books()
    elif choice == "Display Statistics":
        display_statistics()

if __name__ == "__main__":
    main()