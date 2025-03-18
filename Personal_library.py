library = []

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book():
    search_term = input("Enter the title or author to search: ").lower()
    matching_books = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]
    
    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_books():
    if not library:
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics():
    total_books = len(library)
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main_menu():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()