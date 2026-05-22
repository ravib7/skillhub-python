import os

folder_name = input("enter folder name ")
os.makedirs(folder_name, exist_ok=True) # create test name folder