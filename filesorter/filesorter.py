#!/usr/bin/env python3
# This Linux shell program transfers files to folders inside a user's local repository.
# This program makes the assumption that you would like to move ALL files to one folder.

import os
import shutil

def process_paths(path_, folder_):
	"""process_paths() takes a path to an already-existing file in a user's main git repo, 
	and it generates a new path, where the file is in any folder that the user specifies"""
	
	# the path is split into parts based on directories
	alteredpath = path_.split("/")
	
	# the folder specified by the user is inserted into the path
	alteredpath.insert(4, folder_)
	
	# tha path is rejoined
	alteredpath = "/".join(alteredpath)
	
	return path_, alteredpath


# the user specifies what folder the files will be moved to.
folder_name = input("What is the name of the folder you are moving to? > ")

os.chdir("../")
# the filesorter program is stored alone, in its own directory.
# the filesorter moves all files in a specific directory to a different directory
# so it cannot also be part of the directory it is operating on.
# so the program automatically leaves the filesorter's directory

# a path to the specified folder is generated,
# and the number of files is initialised
folder_path = os.path.join(os.getcwd(), folder_name)
number_of_files = 0

# files are only moved if the folder chosen is an already-existing directory
if os.path.isdir(folder_path):
	
	# the current working directory is iterated through, once for each file
	for file in os.listdir(os.getcwd()):
		
		# its current path is given the name 'old_path'
		old_path = os.path.join(os.getcwd(), file)
		
		# if the path of any file is actually a path to a directory, 
		# the directory is skipped, and the program notifies you that it skipped something. 
		if os.path.isdir(old_path):
			print(f"Skipped {old_path}")
		else:
			# a new path is generated for its new location
			old_path, new_path = process_paths(old_path, folder_name)
			
			# and the folder is moved
			shutil.move(old_path, new_path)
			
			# the number of files is counted: one successful loop = one file
			number_of_files += 1
			
	# and after the loop is done, the number of files moved is displayed
	print(f"Moved {number_of_files} files successfully.")
else:
	
	# if the directory, does not exist, the program exits cleanly.
	print("That directory does not exist. No files were moved.")
	print("Check that you haven't misspelled it, or typed in a directory that hasn't been created yet.") 
