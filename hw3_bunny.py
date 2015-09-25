def bunnyEars2(line):
	if(line<= 0):
		return 0
	elif (line % 2 == 1):		#odd bunny has two ears
		totalEars=2
	elif (line % 2 == 0):		#even bunny has three ears
		totalEars=3
	return bunnyEars2(line-1) + totalEars

numBunny=int(input("How many lines of bunnies? "))
if numBunny==0:
		print("bunnyEars2(0) -> 0")
else:
		print("bunnyEars2(" + str(numBunny) + ") ->", bunnyEars2(numBunny))



	
