class Product:
    def __init__(self, name, description, price, availability):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__availability = availability

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_availability(self):
        return self.__availability

    def set_name(self, new_name):
        self.__name = new_name

    def set_description(self, new_description):
        self.__description = new_description

    def set_price(self, new_price):
        self.__price = new_price

    def set_availability(self, new_availability):
        self.__availability = new_availability

if __name__ == "__main__":
    product1 = Product("Laptop", "Powerful laptop for work and entertainment", 1200, True)
    
    print("Name:", product1.get_name())
    print("Description:", product1.get_description())
    print("Price:", product1.get_price(), " $")
    print("Availability:", product1.get_availability())

    product1.set_price(1100)
    print("Updated price:", product1.get_price())
