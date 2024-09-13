import random

def cpu():
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

def game():

    print("First to 3 wins")

    u_pts, c_pts = 0,0

    while(u_pts<3 and c_pts<3):
        print("Choose rock, paper or scissors")
        user = input() 
        user.lower() #To match the casesizes between the computer and the user's input

        comp = cpu()

        if(user == comp):
            print("Computer played: ", comp)
            print("Tie")

        elif((user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper") or (user == "paper" and comp == "rock")):
            print("Computer played: ", comp)
            print("You win")
            u_pts+=1

        elif((comp == "rock" and user == "scissors") or (comp == "scissors" and user == "paper") or (comp == "paper" and user == "rock")):
            print("Computer played: ", comp)
            print("Computer wins")
            c_pts+=1
        #print('\n')

    print("Final score\n","Your points: ", u_pts, "\nComputer's points: ", c_pts)

game()
