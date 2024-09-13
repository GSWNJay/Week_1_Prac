def genNum():
    num = random.randrange(1,100)
    #print("Random num is, ", num)
    return num


def guessNum():
    tries = 3
    answer = genNum()
    guess = 0

    print ("answer: ", answer)

    while(tries>0 and answer != guess):
        
        guess = int(input())

        #print('Guessed: ', guess)
        #print ("answer: ", answer)

        if(answer == guess):
            print("You guessed it correctly")     
        else:
            print("Guess again")

        tries-=1

    if(tries<=0 and answer != guess):
        print("You're out of tries")
        print("The correct guess is: ", answer)

    return

import random

print ("Guess the random number")
guessNum()

