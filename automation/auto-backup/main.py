import os
from datetime import datetime
import time
import shutil

folder_path = os.getcwd()
interval = int(input("enter backup interval in seconds "))
backup_folder = input("enter backup folder name ")
backup_path = os.path.join(r"C:\Users\ADMIN\Desktop\backup-zip",backup_folder)
os.makedirs(backup_path,exist_ok=True)

while True:
    backup_name = f"backup_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}"
    fn = os.path.join(r"C:\Users\ADMIN\Desktop\backup-zip",backup_folder, backup_name)
    shutil.make_archive(fn, "zip", backup_path)
    print("backup compete")
    time.sleep(interval)