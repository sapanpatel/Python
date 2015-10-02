import os
import fnmatch

def fileFinder(dir_path, fileName): 	#function to find the file
	found = 0  #default set as file not found	
	for dirpath, dirs, files in os.walk(dir_path):
		for single_file in files:
			if fnmatch.fnmatch(single_file, fileName):
				print("\n>>The file is found at:",os.path.join(dirpath, single_file), "\n")
				found = 1   #set to 1 if file is found
	return found

initialPath = input("\nEnter the directory path: ")
file_name = input ("\nEnther the file name: ")
foundStatus = fileFinder(initialPath, file_name)
if foundStatus == 0:
	print("\nFile", file_name, "is not found.\n")