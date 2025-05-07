from book import Book 

class Magazine(Book):
    def __init__(self, title, editor, year):
        super().__init__(title, editor, year)
    
    def borrow(self):
        """
        Magazine can't be borrowed 
        """
        return f"{self.title} is a Magazine and cannot be borrowed"