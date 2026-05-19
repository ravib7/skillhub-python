# 10 < 20    20 > 5

# AND
# OR

# True   and   True       T
# False  and   True       F
# True   and   False      F
# False  and   False      F


# True   or   True       T
# False  or   True       T
# True   or   False      T
# False  or   False      F


# num1 = 10
# num2 = 20
num1,num2 = 10,20

print(num1 < num1 and num2 > num1)
print(num1 == num1 or num2 > num1)
print(num1 == num1 or num1 > num1)