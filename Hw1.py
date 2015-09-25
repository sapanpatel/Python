''' Assignment 1 : Mini guessing game '''

name = input("what is your name? ")
print("Hello" + " " +name+ " " + "let us play a game")
print("Guess a random number between 1 to 100 and I will try to guess it")

low=0
high=100
mid=50
count=0
while (True):
        count = count +1
        mid = int ((low+high)/2)
         
        choice=input(print("Is the number " +str(mid) + "? yes/no \n Ans."))
        
        if(choice=="yes"):
                        print("Yeyy! I got it in " +str(count)+ " tries! ")
                        choice2 =input(print("Want to play again? yes/no \n"))
                        if choice2 == "yes":
                                low = 0
                                high = 100
                                mid = 50
                                count = 0
                        else:
                                break
        if(choice == "no"):           
                choice3=input(print("Is the number greater than " +str(mid)+ "? yes/no? \n Ans."))
                if choice3 == "yes":
                        low = mid
                if choice3 == "no":
                        high = mid
                
                                            
