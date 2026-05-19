# file = open("temp.txt", "w")
# # overwrite content
# file.write("Hi There")
# file.close()

# w =>  overwrite content
# a =>  append to existing content
with open("temp.txt", "a") as file:
    file.write("py")