import shelve
from datetime import datetime

d = {"a":"Hello everyone", "b":"This is a test to check which is faster: dictionary or shelve?", "c": (10,11,12), "d": (499,599,699), "e": {1:2, 2:3, 3:4}}

s = shelve.open("Shelve1")
s["a"] = "Hello everyone"
s["b"] = "This is a test to check which is faster: dictionary or shelve?"
s["c"] = (10,11,12)
s["d"] = (499,599,699)
s["e"] = {1: 2, 2: 3, 3:4}

print("-------------------------------------------------------------")
print("Dictionary")
print("-------------------------------------------------------------")
dt1 = datetime.now()
for key, value in d.items():
	print(key, ":", value)
dt2 = datetime.now()
dictionaryTime = dt2-dt1

print("-------------------------------------------------------------")
print("Shelve")
print("-------------------------------------------------------------")
dt3 = datetime.now()
for key, value in s.items():
	print(key, ":", value)
s.close()
dt4 = datetime.now()
shelveTime = dt4 - dt3

print("-------------------------------------------------------------")
print("Result")
print("-------------------------------------------------------------")
print("Dictionary:", dictionaryTime, "\nShelve:", shelveTime, "\n")
if dictionaryTime < shelveTime:
	print("Dictionary is faster.\n")
else:
	print("Shelve is faster.")