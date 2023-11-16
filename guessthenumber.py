import random
a = True

while a == True:  
    randomNumber = random.randrange(1,100)
    print("I have thought of a number between 1 and 100. What is it?")
    isanswercorrect = False
    while isanswercorrect == False:
        guess = input("I think the number is: ")
        if int(randomNumber) == int(guess):
            isanswercorrect = True
            print("You go it! My number was " + str(randomNumber))
            print("")
            print("")
            print("")
            print("Lets play again!")
            print("")
        if int(guess) < int(randomNumber):
            print("Your answer of " + guess + " is lower than the answer, try again!")
        if int(guess) > int(randomNumber):
            print("Your answer of " + guess + " is higher than the answer, try again!")
        #else:
            #print("Sorry, your answer is incorrect! Try again!")
