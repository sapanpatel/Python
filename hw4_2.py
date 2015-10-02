keyword = "password="
fileName = input("\nEnther the path and file name: ")
fileDirectory = open(fileName, "r")
count = 0	#count the number of passwords in the file

print("\n")
for i, line in enumerate(fileDirectory):
	
	if line.find(keyword) != -1:
		print("Found in line", i + 1, ":", line[:50])
		count = count + 1

if count == 0:
	print("\nFile", fileName, "is secure.\n")
else:
	print("\nFile", fileName, "is not secure.\n")