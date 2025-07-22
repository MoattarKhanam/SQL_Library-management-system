from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
        self.borrower_id = None
        self.due_date = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_book_id = None

class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter book ID: ").strip()
        if book_id in self.books:
            print("Book ID already exists.")
            return
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        self.books[book_id] = Book(book_id, title, author)
        print(f"Book '{title}' added.")

    def update_book(self):
        book_id = input("Enter book ID to update: ").strip()
        if book_id not in self.books:
            print("Book not found.")
            return
        title = input("Enter new title: ").strip()
        author = input("Enter new author: ").strip()
        book = self.books[book_id]
        book.title = title
        book.author = author
        print("Book updated.")

    def delete_book(self):
        book_id = input("Enter book ID to delete: ").strip()
        if book_id not in self.books:
            print("Book not found.")
            return
        if not self.books[book_id].available:
            print("Cannot delete a borrowed book.")
            return
        del self.books[book_id]
        print("Book deleted.")

    def search_books(self):
        query = input("Enter title or author to search: ").strip().lower()
        found = False
        for book in self.books.values():
            if query in book.title.lower() or query in book.author.lower():
                status = "Available" if book.available else f"Borrowed (Due: {book.due_date.strftime('%Y-%m-%d')})"
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")
                found = True
        if not found:
            print("No matching books found.")

    def register_member(self):
        member_id = input("Enter member ID: ").strip()
        if member_id in self.members:
            print("Member ID already exists.")
            return
        name = input("Enter member name: ").strip()
        self.members[member_id] = Member(member_id, name)
        print(f"Member '{name}' registered.")

    def borrow_book(self):
        member_id = input("Enter member ID: ").strip()
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        if member.borrowed_book_id is not None:
            print("Member already has a borrowed book.")
            return
        book_id = input("Enter book ID to borrow: ").strip()
        if book_id not in self.books:
            print("Book not found.")
            return
        book = self.books[book_id]
        if not book.available:
            print("Book is currently borrowed.")
            return
        book.available = False
        book.borrower_id = member_id
        book.due_date = datetime.now() + timedelta(days=14)
        member.borrowed_book_id = book_id
        print(f"Book '{book.title}' borrowed by {member.name}. Due date is {book.due_date.strftime('%Y-%m-%d')}.")

    def return_book(self):
        member_id = input("Enter member ID: ").strip()
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        if member.borrowed_book_id is None:
            print("Member has no borrowed book.")
            return
        book_id = member.borrowed_book_id
        book = self.books[book_id]
        book.available = True
        book.borrower_id = None
        book.due_date = None
        member.borrowed_book_id = None
        print(f"Book '{book.title}' returned by {member.name}.")

    def show_all_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books.values():
            status = "Available" if book.available else f"Borrowed (Due: {book.due_date.strftime('%Y-%m-%d')})"
            print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def show_all_members(self):
        if not self.members:
            print("No members registered.")
            return
        for member in self.members.values():
            borrowed = member.borrowed_book_id if member.borrowed_book_id else "None"
            print(f"ID: {member.member_id}, Name: {member.name}, Borrowed Book ID: {borrowed}")

def main():
    system = LibrarySystem()
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Books")
        print("5. Register Member")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Show All Books")
        print("9. Show All Members")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.add_book()
        elif choice == "2":
            system.update_book()
        elif choice == "3":
            system.delete_book()
        elif choice == "4":
            system.search_books()
        elif choice == "5":
            system.register_member()
        elif choice == "6":
            system.borrow_book()
        elif choice == "7":
            system.return_book()
        elif choice == "8":
            system.show_all_books()
        elif choice == "9":
            system.show_all_members()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

