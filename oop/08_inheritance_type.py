# Multi Level Inheritance

class Test:
    def say_hello(self):
        print("hello")

class Computer:     # single level
    def __init__(self, processor, ram, ssd):
        self.processor = processor 
        self.ram = ram 
        self.ssd = ssd

class Laptop(Computer): # multi level
    def __init__(self, processor, ram, ssd, brand):
        super().__init__(processor, ram, ssd)
        self.brand = brand

class GamingLaptop(Laptop, Test): # multiple level
    def __init__(self, processor, ram, ssd, brand, gpu):
        super().__init__(processor, ram, ssd, brand)
        self.gpu = gpu
    
# L1 = Laptop("intel i5", "16GB", "1TB", "Dell")
# print(L1.brand)

G1 = GamingLaptop("intel i5", "16GB", "1TB", "Dell", "Nvidia")
print(G1.processor)
print(G1.ram)
print(G1.ssd)
print(G1.brand)
print(G1.gpu)
G1.say_hello()

