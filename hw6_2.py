from random import randrange

print (" Interger Division")
while(1):
    a= randrange(20)
    b= randrange(5)
    try:
        ans = (a/b)
    except:
        ans = -1
    print ("",a,"/",b,"=",)
    number = input("")
    try:
        if int(ans) == int(number):
            print ("CORRECT!")
        else:
            print("INCORRECT")
    except ValueError:
        print("Please enter Integers Only!")