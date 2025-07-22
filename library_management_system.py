import datetime

# --------- Data Storage ---------
# Using lists to store books, members, and borrowing records in memory
books = []
members = []
borrowed_books = []

# --------- Helper Functions ---------

def find_book(book_id):
    """Find a book in the collection by its ID."""
    for book in books:
        if book['id'] == book_id:
            return book
    return None

def find_member(member_id):
    """Find a member by their ID."""
    for member in members:
        if member['id'] == member_id:
            return member
    return None

def calculate_due_date():
    """Calculate due date as 14 days from today."""
    return datetime.date.today() + datetime.timedelta(days=14)

# --------- Core Features ---------

def add_book():
    """Add a new book to the system."""
    book_id = input("Enter Book ID: ").strip()
    if find_book(book_id):
        print("⚠️ Book ID already exists. Try updating the book instead.")
        return
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()
    try:
        copies = int(input("Enter number of copies: ").strip())
    except ValueError:
        print("❌ Please enter a valid number for copies.")
        return
    books.append({'id': book_id, 'title': title, 'author': author, 'copies': copies})
    print("✅ Book added successfully.")

def update_book():
    """Update existing book information."""
    book_id = input("Enter Book ID to update: ").strip()
    book = find_book(book_id)
    if not book:
        print("⚠️ Book not found.")
        return
    title = input(f"Enter new Title (leave blank to keep '{book['title']}'): ").strip()
    author = input(f"Enter new Author (leave blank to keep '{book['author']}'): ").strip()
    copies_input = input(f"Enter new Number of copies (leave blank to keep {book['copies']}): ").strip()
    
    if title:
        book['title'] = title
    if author:
        book['author'] = author
    if copies_input:
        try:
            book['copies'] = int(copies_input)
        except ValueError:
            print("❌ Invalid number of copies entered. Update aborted.")
            return
    print("✅ Book updated successfully.")

def delete_book():
    """Delete a book from the system."""
    book_id = input("Enter Book ID to delete: ").strip()
    book = find_book(book_id)
    if not book:
        print("⚠️ Book not found.")
        return
    books.remove(book)
    print(f"✅ Book '{book['title']}' deleted successfully.")

def search_book():
    """Search for books by title keyword."""
    keyword = input("Enter book title to search: ").strip().lower()
    found_books = [book for book in books if keyword in book['title'].lower()]
    if not found_books:
        print("No books found with that title keyword.")
        return
    print(f"📚 Found {len(found_books)} book(s):")
    for book in found_books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Copies: {book['copies']}")

def view_all_books():
    """Display all books and their availability."""
    if not books:
        print("No books in the system.")
        return
    print("📚 List of all books:")
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Copies Available: {book['copies']}")

def register_member():
    """Register a new library member."""
    member_id = input("Enter Member ID: ").strip()
    if find_member(member_id):
        print("⚠️ Member ID already exists.")
        return
    name = input("Enter Member Name: ").strip()
    members.append({'id': member_id, 'name': name})
    print("✅ Member registered successfully.")

def borrow_book():
    """Allow a member to borrow a book if available."""
    member_id = input("Enter Member ID: ").strip()
    member = find_member(member_id)
    if not member:
        print("⚠️ Member not found. Please register first.")
        return
    book_id = input("Enter Book ID: ").strip()
    book = find_book(book_id)
    if not book:
        print("⚠️ Book not found.")
        return
    if book['copies'] < 1:
        print("❌ No copies available for borrowing.")
        return
    # Deduct one copy since it's borrowed
    book['copies'] -= 1
    due_date = calculate_due_date()
    borrowed_books.append({'member_id': member_id, 'book_id': book_id, 'due_date': due_date})
    print(f"✅ Book borrowed successfully. Due date is {due_date}.")

def return_book():
    """Process returning a borrowed book."""
    member_id = input("Enter Member ID: ").strip()
    book_id = input("Enter Book ID: ").strip()
    borrowed = None
    for record in borrowed_books:
        if record['member_id'] == member_id and record['book_id'] == book_id:
            borrowed = record
            break
    if not borrowed:
        print("⚠️ No borrowing record found for this member and book.")
        return
    borrowed_books.remove(borrowed)
    book = find_book(book_id)
    if book:
        book['copies'] += 1  # Return one copy to available stock
    print("✅ Book returned successfully.")

def view_borrowed_books():
    """Display all borrowed books with member info and due dates."""
    if not borrowed_books:
        print("No books are currently borrowed.")
        return
    print("📖 Borrowed Books:")
    for record in borrowed_books:
        member = find_member(record['member_id'])
        book = find_book(record['book_id'])
        print(f"Member: {member['name']} (ID: {member['id']}) | Book: {book['title']} (ID: {book['id']}) | Due Date: {record['due_date']}")

# --------- Main Menu Loop ---------

def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n📚 Library Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. View All Books")
        print("6. Register Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. View Borrowed Books")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_book()
        elif choice == '5':
            view_all_books()
        elif choice == '6':
            register_member()
        elif choice == '7':
            borrow_book()
        elif choice == '8':
            return_book()
        elif choice == '9':
            view_borrowed_books()
        elif choice == '0':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 0 to 9.")

if __name__ == "__main__":
    main_menu()
