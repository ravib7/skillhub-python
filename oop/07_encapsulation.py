# encapsulation => hiding things
class Laptop:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
    
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def update_price(self, new_price):
        self.__price = new_price


L1 = Laptop("Dell", "xps", 98000)
print(L1.get_brand())
print(L1.get_price())
L1.update_price(5000)
print(L1.get_price())
