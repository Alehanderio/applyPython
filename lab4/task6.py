class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def display_info(self):
        pass

class Fiction(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre
    
    def display_info(self):
        print(f"Fiction book: {self.title} by {self.author}, genre: {self.genre}")

class Science(Book):
    def __init__(self, title, author, field):
        super().__init__(title, author)
        self.field = field
    
    def display_info(self):
        print(f"Science book: {self.title} by {self.author}, field: {self.field}")

class Children(Book):
    def __init__(self, title, author, age_range):
        super().__init__(title, author)
        self.age_range = age_range
    
    def display_info(self):
        print(f"Children's book: {self.title} by {self.author}, age range: {self.age_range}")

books = [
    Fiction("A Game of Thrones", "George R.R. Martin", "fantasy"),
    Science("A Brief History of Time", "Stephen Hawking", "astrophysics"),
    Children("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "6-10 years")
]

for book in books:
    book.display_info()
