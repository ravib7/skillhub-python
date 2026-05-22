import os
import shutil

# folder_name = os.getcwd()
folder_name = input("enter folder path ")

file_type = {
    "picture":["png","jpg","jpeg"],
    "audio":["mp3"],
    "video":["mp4"],
    "doc":["pdf","docx","csv","txt"],
    "python":["py"]
}

# for key, value in file_type.items(): #return tuple
#     print(key,value)


# arr = ["png","jpg","jpeg"]
# if "jpg" in arr:
#     print("ahe")
# else:
#     print("nahi")


files = os.listdir(folder_name)

for item in files:
    moved = False
    ext = item.split(".")[-1]
    for key, value in file_type.items():
        if ext in value:
            # os.makedirs(key, exist_ok=True) # create folder
            # shutil.move(item, key)
            os.makedirs(os.path.join(folder_name,key), exist_ok=True) # create folder
            shutil.move(os.path.join(folder_name,item), os.path.join(folder_name,key))
            print(f"{item} moved to {key}")
            moved = True

    if not moved:
            os.makedirs(os.path.join(folder_name,"other"), exist_ok=True) # create folder
            shutil.move(os.path.join(folder_name,item), os.path.join(folder_name,"other"))
            print(f"{item} moved to other")