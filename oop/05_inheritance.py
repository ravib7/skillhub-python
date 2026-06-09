# class Computer:
#     ram = "8gb"
#     ssd = "512gb"
#     processor = "intel i7"

# class Laptop(Computer):
#     pass

# #       👇Chiled  👇Parent
# class Desktop(Computer):
#     pass

# L1 = Laptop()
# print(L1.processor)

# D1 = Desktop()
# print(D1.ram)


class Computer:
    def __init__(self, ram, ssd):
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def __init__(self, ram, ssd, processor):
        super().__init__(ram, ssd)  # call parent constructor (Computer)
        # self.ram = ram
        # self.ssd = ssd
        self.processor = processor

class Desktop(Computer):
    def __init__(self, ram, ssd, brand):
        super().__init__(ram, ssd)
        self.brand = brand

L1 = Laptop("8gb", "512gb", "intel 17")
D1 = Desktop("16GB", "1TB", "Asus")
print(L1.ram, L1.ssd)
print(D1.ram, D1.ssd)

# print(D1.brand)
# print(L1.processor)