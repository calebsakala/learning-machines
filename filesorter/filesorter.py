#!/usr/bin/env python3

import os
import shutil

def process_paths(path_, folder_):
	alteredpath = path_.split("/")
	alteredpath.insert(4, folder_)
	alteredpath = "/".join(alteredpath)
	return path_, alteredpath


folder_name = input("What is the name of the folder you are moving to? > ")
os.chdir("../")
folder_path = os.path.join(os.getcwd(), folder_name)
number_of_files = 0


if os.path.isdir(folder_path):
	for file in os.listdir(os.getcwd()):
		old_path = os.path.join(os.getcwd(), file)
		if os.path.isdir(old_path):
			print(f"Skipped {old_path}")
		else:
			old_path, new_path = process_paths(old_path, folder_name)
			shutil.move(old_path, new_path)
			number_of_files += 1
	print(f"Moved {number_of_files} files successfully.")
else:
	print("That is not a valid directory. Operation failed.")
