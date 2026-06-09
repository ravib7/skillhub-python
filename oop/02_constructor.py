class Laptop:

    # 1 Deafult constructor
    """
      def __init__(self):
           pass
    """


    category = "computer" # class property (variable)
# 2 Parameterized constructor
        #         👇 calling object
    def __init__(self, name):
        # print(self)
        self.brand = name  # instance property (variable)
        print("constructor")

b1 = Laptop("dell") # constructor
b2 = Laptop("apple") # constructor
# print(b1.category)
print(b1.brand)
print(b2.brand)
