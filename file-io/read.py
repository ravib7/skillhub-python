# file = open("temp.txt", "r") # open file in read mode

# data = file.read() # read file
# print(data)

# file.close() # always close file

with open("temp.txt", "r") as file:
    data = file.read()
    print(data)