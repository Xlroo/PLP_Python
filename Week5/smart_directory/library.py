from book import Book

class Library:
    def __init__(self, name):
        """
        Create a new library with a name and an emplty list of books
        """
        self.name = name
        self.books = []
    
    def add_book(self,book):
        """
        Add a book object to the library's connection
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Return a list of all books with their details
        """
        return[book.get_details() for book in self.books]
    
    def find_book(self, title):
        """
        Search for a book by title (case-insensitive).
        If found, return the object. If not return none.
        """
        for book in self.books:
            if book.title.lower()== title.lower():
                return book
            return None