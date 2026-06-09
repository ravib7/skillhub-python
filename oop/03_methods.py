class Laptop:
    def __init__(self, name, hq, country):
        self.brand = name
        self.head = hq
        self.origin = country

    def show(self):
        print(f"brand = {self.brand}")
    
    def get_data(self):
        return {"brand": self.brand, "head":self.head, "origin":self.origin}

b1 = Laptop("dell", "new york", "usa")
b2 = Laptop("lenovo", "shanghai", "china")
# print(b2.origin)

b1.show()
result = b2.get_data()
print(result)