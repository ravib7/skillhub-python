balance = 10000
pin = 1234

user_pin = int(input("Please enter your pin number ")) # 1234

if (pin == user_pin) :
    print("welcome")
    while True :
        print("-------------- ATM MENU --------------")
        print("1. Check Balance")
        print("2. Widraw")
        print("3. Deposit")
        print("4. Exit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            print(f"your balance is {balance}")
        elif choice == 2:
            amount = int(input("Enter Amount "))
            if amount > balance:
                print("insufficient balance")
            else:
                balance = balance -amount
        elif choice == 3:
            amount = int(input("enter amount "))
            balance = balance + amount
        elif choice == 4:
            print("Thank You")
            break
        else:
            print("Invalid Choice")
else:
    print("invalid pin")
