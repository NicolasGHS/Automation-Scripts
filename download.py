#!/usr/bin/python3

import os

home_dir = os.path.expanduser("~")
path = os.path.join(home_dir, "Downloads")

downloads_list = os.listdir(path)

zip_extension = ".zip"
deb_extension = ".deb"
appImage_extension = ".AppImage"


for file in downloads_list:
    if zip_extension in file:
        os.rename(f"{path}/{file}", f"{path}/zips/{file}")
        print(f"Succesfully moved {file}.")

for file in downloads_list:
    if deb_extension in file:
        os.rename(f"{path}/{file}", f"{path}/debs/{file}")
        print(f"Succesfully moved {file}.")

for file in downloads_list:
    if appImage_extension in file:
        os.rename(f"{path}/{file}", f"{path}/appImages/{file}")
        print(f"Succefully moved {file}.")

for file in downloads_list:
    if zip_extension not in file and deb_extension not in file and appImage_extension not in file:
        if "." in file:
            os.rename(f"{path}/{file}", f"{path}/_na-te-kijken/{file}")

            print(f"Succesfully moved: {file}")