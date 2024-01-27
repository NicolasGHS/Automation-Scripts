#!/usr/bin/python3

import os

home_dir = os.path.expanduser("~")
path = os.path.join(home_dir, "Downloads")

downloads_list = os.listdir(path)

zip_extension = ".zip"

for file in downloads_list:
    if zip_extension in file:
        os.rename(f"{path}/{file}", f"{path}/zips/{file}")
        print(f"Succesfully moved {file}.")
