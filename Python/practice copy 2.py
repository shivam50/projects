import random

start = int(input("Let's Play Hangman , press 1 to begin\n"))

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


if start == 1:
    print('''
            _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                    |___/                       
    ''')

    print("\nYour job is to save the hangman from hanging, \n Every wrong answer will bring the hangman close to hanging, \n When all the lives are finished, hangman will die and you will lose")

    lives = 6
    trial = 0

#    with open("words.txt") as file:
#       word_list = file.read().splitlines()

    # getting random word
    word_list = ["babuna", "timki", "kantan", "Chotababu", "Gattabaabu"]
    temp_word = random.choice(word_list)

    #printing blanks and hangmam
    i = 0
    blindex = []
    while i <= (len(temp_word)-1):
       blindex.append("_")
       i += 1
    
    refresh = blindex
    print(" ".join(blindex))
    print(f"Your hangman is : {HANGMANPICS[0]}")

    guessed_letters = []


  #game logic
    while lives > 0:
      letter = input("Let's bring it!! what's ur letter guess???")
      
      for i in range (0, len(blindex)):
        if temp_word[i] == letter:
          print("Right guess")
          print(blindex)
                    
        else:
          print("Wrong guess, 1 life taken")
          print(lives)
          lives -= 1
          trial += 1

        print("\n" + " ".join(blindex))  
        print(f"Your hangman right now: {HANGMANPICS[trial]}")




            

        

