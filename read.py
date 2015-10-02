import shelve

def readData(user):
	userData = {}
	for name, info in user.items():
		#iterate shelve, read data and store in dictionary
		userData[name] = info
	return userData