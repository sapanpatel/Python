def count_frequency(myList):
	dictionary = { }
	for word in myList:
		if word not in list( dictionary.keys() ):
			dictionary.update( {word: 1 } )
		else:
			dictionary.update( {word: dictionary[word] + 1} )
	return dictionary

mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]

print (count_frequency(mylist))