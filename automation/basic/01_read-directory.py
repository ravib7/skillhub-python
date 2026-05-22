import os

current_folder = os.getcwd() # cwd current working directory
print(current_folder)

files = os.listdir(current_folder)
print(files)