class Book:
    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author = author
        self.genre = genre
        self.copies = copies

class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    def add_book(self, book):
        self.books.append(book)

    def increase_copies(self, book_title, num_copies):
        for book in self.books:
            if book.title == book_title:
                book.copies += num_copies
                break

    def search_book(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in book.genre.lower():
                results.append(book)
        return results

    def add_member(self, name, phone):
        self.members[name] = phone

    def rent_book(self, member_name, book_title):
        # Implement logic for renting a book to a member
        pass

    def calculate_fine(self, member_name):
        # Implement logic for calculating fines
        pass

# Example usage:
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 3)
library.add_book(book1)
library.add_book(book2)

# Add a member
library.add_member("John Doe", "123-456-7890")

# Search for a book
search_results = library.search_book("Gatsby")
for book in search_results:
    print(f"Title: {book.title}, Author: {book.author}, Copies: {book.copies}")