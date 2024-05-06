class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)

class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn):
        super().__init__(title, author, publication_year)
        self.isbn = isbn

    def display_info(self):
        super().display_info()
        print("ISBN:", self.isbn)

class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.issue_number)

class Other(LibraryItem):
    def __init__(self, title, author, publication_year, item_type):
        super().__init__(title, author, publication_year)
        self.item_type = item_type

    def display_info(self):
        super().display_info()
        print("Item Type:", self.item_type)

def add_library_item():
    print("Enter the type of item you want to add (Book, Magazine, Other):")
    item_type = input().strip()
    if item_type.lower() == 'book':
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        isbn = input("Enter ISBN: ")
        return Book(title, author, publication_year, isbn)
    elif item_type.lower() == 'magazine':
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        issue_number = input("Enter issue number: ")
        return Magazine(title, author, publication_year, issue_number)
    elif item_type.lower() == 'other':
        title = input("Enter title: ")
        author = input("Enter author: ")
        publication_year = input("Enter publication year: ")
        item_type = input("Enter item type: ")
        return Other(title, author, publication_year, item_type)
    else:
        print("Invalid item type.")

def observe_library_item(item):
    item.display_info()

# Example usage:
if __name__ == "__main__":
    library_items = []

    while True:
        print("\n1. Add library item")
        print("2. Observe library item")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = add_library_item()
            library_items.append(item)
            print("Library item added successfully.")
        elif choice == '2':
            if len(library_items) == 0:
                print("No library items to observe.")
            else:
                print("\nLibrary items:")
                for i, item in enumerate(library_items):
                    print(f"{i + 1}. {item.title}")
                selection = int(input("Enter the number of the item you want to observe: "))
                if 1 <= selection <= len(library_items):
                    observe_library_item(library_items[selection - 1])
                else:
                    print("Invalid selection.")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
