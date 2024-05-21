from abc import ABC, abstractmethod

class LibraryElement(ABC):
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryElement):
    def __init__(self, title, author, publication_year, publisher, isbn):
        super().__init__(title, author, publication_year)
        self.publisher = publisher
        self.isbn = isbn

    def display_info(self):
        print(f"Book: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}\nPublisher: {self.publisher}\nISBN: {self.isbn}")


class Magazine(LibraryElement):
    def __init__(self, title, author, publication_year, volume, issue):
        super().__init__(title, author, publication_year)
        self.volume = volume
        self.issue = issue

    def display_info(self):
        print(f"Magazine: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}\nVolume: {self.volume}\nIssue: {self.issue}")


class Other(LibraryElement):
    def __init__(self, title, author, publication_year, description):
        super().__init__(title, author, publication_year)
        self.description = description

    def display_info(self):
        print(f"Other: {self.title}\nAuthor: {self.author}\nYear: {self.publication_year}\nDescription: {self.description}")



library_items = [
    Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "George Allen & Unwin", "9780261102385"),
    Magazine("National Geographic", "Various Authors", 2021, "Vol. 240", "No. 5"),
    Other("Map of Middle-Earth", "J.R.R. Tolkien", 1954, "Detailed map from The Lord of the Rings")
]

for item in library_items:
    item.display_info()
    print()
