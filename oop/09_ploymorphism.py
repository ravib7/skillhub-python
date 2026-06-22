class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print("Laptop")
        print(f"Brand {self.brand} Price {self.price}")
    
class GamingLaptop(Laptop):
    # pass
    def show_info(self):
        print("Gaming")
        print(f"Brand {self.brand} Price {self.price}")

L1 = Laptop("dell", 100)
G1 = GamingLaptop("Asus", 200)

L1.show_info()
G1.show_info()

