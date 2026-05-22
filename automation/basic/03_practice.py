import os

def getExt(string):
    return string.split(".")[-1]

current_folder =os.getcwd()
files = os.listdir(current_folder)
for item in files:
    print(getExt(item))
