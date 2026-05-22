import shutil
import os

FOLDER_PATH = os.getcwd()

file_name = os.path.join(FOLDER_PATH,"backup")

#create zip file👇    👇base name        👇destination
shutil.make_archive(file_name,"zip",FOLDER_PATH)
#                               👆 type