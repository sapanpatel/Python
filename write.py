import shelve
import read

user = shelve.open("testUser")
while True:
	name = input("Enter the name: ")
	if not name:	
		break
	age = input("Enter the age: ")
	country = input("Enter the country of origin: ")

	user[name] = (age, country)	 

userData = read.readData(user)	#read data back from shelve using the function in read.py file
print(userData)

user.clear()	
user.close()	