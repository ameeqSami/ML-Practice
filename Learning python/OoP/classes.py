class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def show_inventory(self):
        print(f"\n--- {self.name} Inventory ---")
        for book in self.books:
            print(book)
        print("---------------------------\n")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"Success! You've checked out {book.title}.")
                    return
                else:
                    print(f"Sorry, {book.title} is already checked out.")
                    return
        print(f"Error: '{title}' not found in our system.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.is_available = True
                print(f"Thank you for returning {book.title}.")
                return
        print("This book does not belong to our library.")


# --- Testing the Code ---
my_library = Library("City Central Library")

# Creating book objects
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("1984", "George Orwell")
b3 = Book("The Hobbit", "J.R.R. Tolkien")

# Using library methods
my_library.add_book(b1)
my_library.add_book(b2)
my_library.add_book(b3)

my_library.show_inventory()

my_library.lend_book("1984")
my_library.lend_book("1984")  # Testing the "already checked out" logic
my_library.show_inventory()

my_library.return_book("1984")
my_library.show_inventory()