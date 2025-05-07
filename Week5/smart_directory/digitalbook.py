from book import Book
class DigitalBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def stream(self):
        """
        Simulates streaming of the digital book
        """
        return f"Streaming {self.title} - Size: {self.file_size}MB"
    
    def borrow(self):
        """
        Overrides the borrow method to reflect digital avialbility
        """
        return f"{self.title} is a digital. No need to borrow  - stream anytime"