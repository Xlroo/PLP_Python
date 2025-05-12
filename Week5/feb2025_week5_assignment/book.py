# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).

class Book:
    def __init__(self, title, author, year ):
        """
        Constructor method to initialize the book
        """
        self.title = title #instance variable
        self.author = author
        self.year = year
        self.available = True
    
    def borrow(self):
        """
        Method for borrowing the book
        """
        if self.available:
            self.available = False
            return f"You have borrowed {self.title}"
        else :
            return f"'{self.title}' is not available for borrowing"
        
    def return_book(self):
        """
        Method to return a borrowed book
        """
        self.available = True
        return f"'{self.title}'has been returned. "
    
    def get_details(self):
        """
        Method to get details about a book
        """
        return f"{self.title} by {self.author} {self.year}."
    
    def set_rating(self,rating):
        """
        Method to rate a book from 0 to 5
        """
        if 0 <= rating <= 5:
            self.__rating = rating
        else :
            print("Rating must be between 0 and 5") #when do we use return and print
    def get_rating(self):
        """
        Get rating of the book
        """
        return self.__rating
