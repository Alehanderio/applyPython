class Car:
    def __init__(self, brand, model, year, mileage):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def set_model(self, new_model):
        self.__model = new_model

    def set_year(self, new_year):
        self.__year = new_year

    def set_mileage(self, new_mileage):
        if new_mileage >= self.__mileage:
            self.__mileage = new_mileage
        else:
            print("Milage cannot be reduced.")




if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 15000)
    
    print("Brand:", car1.get_brand())
    print("Model:", car1.get_model())
    print("Year:", car1.get_year())
    print("Milage:", car1.get_mileage())

    car1.set_mileage(18000)
    print("New Milage:", car1.get_mileage())
