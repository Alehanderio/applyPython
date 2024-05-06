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
        print(f"Художня книга: {self.title} автора {self.author}, жанр: {self.genre}")

class Science(Book):
    def __init__(self, title, author, field):
        super().__init__(title, author)
        self.field = field
    
    def display_info(self):
        print(f"Наукова книга: {self.title} автора {self.author}, галузь: {self.field}")

class Children(Book):
    def __init__(self, title, author, age_range):
        super().__init__(title, author)
        self.age_range = age_range
    
    def display_info(self):
        print(f"Дитяча книга: {self.title} автора {self.author}, вікова категорія: {self.age_range}")

books = [
    Fiction("Гра престолів", "Джордж Мартін", "фентезі"),
    Science("Космічний експрес", "Стефен Хокінг", "астрофізика"),
    Children("Гаррі Поттер і філософський камінь", "Джоан Роулінг", "6-10 років")
]

for book in books:
    book.display_info()
