def drawMan(n):
    Levels = [
    r"""__""",
    r"""__|""",
    r"""__|__""",
    r"""
      |
    __|__
    """,
    r"""
      |
      |
    __|__
    """,
    r"""
      |
      |
      |
    __|__
    """,
    r"""
      |
      |
      |
      |
    __|__
    """,
    r"""
       __
      |
      |
      |
      |
    __|__
    """,
    r"""
       ____
      |
      |
      |
      |
    __|__
    """,
    r"""
       ____
      |    |
      |
      |
      |
    __|__
    """,
    r"""
       ____
      |    |
      |    O
      |
      |
    __|__
    """,
    r"""
       ____
      |    |
      |    O
      |    |
      |
    __|__
    """,
    r"""
       ____
      |    |
      |    O
      |   /|
      |
    __|__
    """,
    r"""
       ____
      |    |
      |    O
      |   /|\
      |
    __|__
    """,
    r"""
       ____
      |    |
      |    O
      |   /|\
      |   / 
    __|__
    """,   
    r"""
       ____
      |    |
      |    O
      |   /|\
      |   / \
    __|__
    """]
    return print(Levels[n])

def secretWord():
    word = input("Enter the secret word to begin hangman: " )
    word = word.lower()
    letters = list(str(word)) #Split word into letters
    return letters 

def play_game():
    
    correct_letters = secretWord()
    os.system('clear')
    size = int(len(correct_letters))
    word_inc = size*"_ "
    print(word_inc, "\n")
    temp = size*"_"
    guessed = list(temp)

    N = -1
    correct = False
    found = False

    while(N < 15 and correct == False):
        guess = input("Guess a letter or the whole word: " )
        guess = guess.lower()

        if(list(guess) == correct_letters):
           correct = True
           guessed = correct_letters
           print("You guessed the whole word correctly")
        elif(len(guess) > 1):
            N+=1
            print("Incorrect guess of the whole word")
        else:
          for i in range(size):
              if(guess == correct_letters[i] and guessed[i] == "_"):
                  guessed[i] = guess
                  found = True
                  print("Correct guess!!\n")
                  break
          if(found == False):
            N+=1
            print("Incorrect guessed letter\n")
          else:
              found = False
            
        if(N>=15):
            drawMan(N)
            print("Game over, this man hanged himself")
        elif(N>-1):
            drawMan(N)
        print("\n")
                  
        print(guessed)
        if(guessed == correct_letters):
            print("All the letter are correct!! Mans survived Franklin.")
            correct = True

import os
play_game()