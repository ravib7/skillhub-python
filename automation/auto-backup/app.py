import os
from datetime import datetime
import shutil
import time

source = input("enter source folder path ")
destination = input("enter backup destination path ")
interval = int(input("enter backup interval in second "))

os.makedirs(destination, exist_ok=True)

while True:
    backup_name = f"backup{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}"

    zip_path = os.path.join(destination, backup_name)
    shutil.make_archive(zip_path, "zip", source)
    print("backup complete")
    time.sleep(interval)
