'''
1. add expense
2. add income
3. view history
4. exit
'''


print("welcome to budget planner")
print("1} Add Income")
print("2} Add Expense")
print("3} View")
print("4} Exit")

while True:
    choice = int(input("please select option 1/2/3/4 "))
    if choice == 1:
        amount = input("enter amount ")
        with open("income.txt", "a") as file:
            file.write(amount)
        print("income added")
    elif choice == 2:
        amount = int(input("enter amount "))
        with open("expense.txt", "w") as file:
            file.write(amount)
        print("expense added")
    elif choice == 3:
        with open("income.txt", "r") as file:
            print(f"income {file.read()}")
    elif choice == 4:
        print("thank you for used budget planner")
        break
    else:
        print("invalid choice")