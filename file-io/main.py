'''
1. add expense
2. add income
3. view history
4. exit
'''

def handleView(file_name):
    total_income = 0
    try:
        with open(file_name, "r") as file:
            income_data = file.readlines()
            for item in income_data:
                amt = int(item.strip().split()[-1])
                total_income = total_income + amt
        return total_income
    except:
        print("error while reading income.txt")
        

def handle_append(file_name):
    income_amount = int(input("enter amount "))
    income_from = input("enter from ")
    try:
        with open(file_name, "a") as file:
            file.write(f"{income_from} {income_amount}\n")
        print("added")
    except:
        print("something went wrong")


def handle_reset(file_name):
    try:
        with open(file_name, "w") as file:
            file.write("")
            print("reset successfully")
    except:
        print("error while reset")
        

print("welcome to budget planner")
print("1} Add Income")
print("2} Add Expense")
print("3} View")
print("4} Reset Income")
print("5} Reset Expense")
print("6} Exit")

while True:
    choice = int(input("please select option 1/2/3/4/5/6 "))
    if choice == 1:
        handle_append("income.txt")
    elif choice == 2:
        handle_append("expense.txt")
    elif choice == 3:
        inc = handleView("income.txt")
        exp = handleView("expense.txt")
        print(f"income: {inc}")
        print(f"expense: {exp}")
        print(f"balance: {inc - exp}")
    elif choice == 4:
        handle_reset("income.txt")
    elif choice == 5:
       handle_reset("expense.txt")
    elif choice == 6:
        print("thank you for used budget planner")
        break
    else:
        print("invalid choice")
