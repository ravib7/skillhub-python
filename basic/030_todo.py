# notes = ["learn pandas", "learn python", "master python"]
# # notes.append("Learn Numpy")
# # notes.insert(0,"Learn Numpy")
# notes.pop(1)
# print(notes)

notes = []

print("1. Add Note")
print("2. View Notes")
print("3. Delete Note")
print("4. Exit")
while True:
    try:
        choice = int(input("Enter Your Choice ")) #1
        if choice == 1:
            task = input("Please Enter Task ")
            notes.append(task)
            print("Task Created Successfully")
        elif choice == 2:
            print(notes)
        elif choice == 3:
            index = int(input("Enter Index Number "))
            notes.pop(index)
            print("Note Deleted Successfully")
        elif choice == 4:
            print("Thank You For Using Todo App")
            break
        else:
            print("invalid choice")
    except:
        print("something went wrong")