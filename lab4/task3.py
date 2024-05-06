class Department:
    def __init__(self, name, budget, personnel):
        self.name = name
        self.budget = budget
        self.personnel = personnel

    def manage_personnel(self):
        print ("The department manages personnel")
        pass

    def manage_budget(self):
        print ("The department manages budget")
        pass





class Finance(Department):
    def __init__(self, name, budget, personnel):
        super().__init__(name, budget, personnel)

    def manage_personnel(self):
        print("Finance manages personnel...")
        pass

    def manage_budget(self):
        print("Finance manages budget...")
        pass

class Marketing(Department):
    def __init__(self, name, budget, personnel):
        super().__init__(name, budget, personnel)

    def manage_personnel(self):
        print("Marketing manages personnel...")
        pass

    def manage_budget(self):
        print("Marketing manages budget...")
        pass

class ProductDevelopment(Department):
    def __init__(self, name, budget, personnel):
        super().__init__(name, budget, personnel)

    def manage_personnel(self):
        print("ProductDevelopment manages personnel...")
        pass

    def manage_budget(self):
        print("ProductDevelopment manages budget...")
        pass

# Example usage:
if __name__ == "__main__":
    finance_dept = Finance("Finance", 1000000, 20)
    marketing_dept = Marketing("Marketing", 800000, 15)
    product_dev_dept = ProductDevelopment("Product Development", 1500000, 30)

    finance_dept.manage_personnel()
    finance_dept.manage_budget()

    marketing_dept.manage_personnel()
    marketing_dept.manage_budget()

    product_dev_dept.manage_personnel()
    product_dev_dept.manage_budget()
