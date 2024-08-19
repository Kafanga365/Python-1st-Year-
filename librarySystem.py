class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is not available for borrowing.")

    def returnBook(self):
        self.available = True
        print(f"{self.title} has been returned.")


class DigitalBook(Book):
    def __init__(self, title, author, isbn, compatibility):
        super().__init__(title, author, isbn)
        self.compatibility = [compatibility]

    def addCompatibility(self, compatibility):
        self.compatibility.append(compatibility)


class Library:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def displayLibrary(self):
        for book in self.books:
            availability = "Available" if book.available else "Not available"
            print(f"{book}: {availability}")


def testLibrary():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    digitalBook = DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")

    library.addBook(book1)
    library.addBook(book2)
    library.addBook(digitalBook)

    digitalBook.addCompatibility("PDF")
    digitalBook.addCompatibility("Apple")

    book1.borrow()
    digitalBook.borrow()
    book1.returnBook()

    library.displayLibrary()


testLibrary()