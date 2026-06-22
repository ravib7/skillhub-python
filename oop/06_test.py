# create a class called as calculator
# add parameterized constructor with two values num1 and num2
# create 4 methods add, sub, mul and div which will perform calculation
# finally create object called dummy
# and call all the methods from dummy object


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
       return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

dummy = Calculator(100,10)

sum = dummy.add()
diff = dummy.sub()
pro = dummy.mul()
qou = dummy.div()

print(sum, diff, pro, qou)
