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
    word_list = ["babuna", "timki", "kantan", "Chotababu", "Gattabaabu"]
    

    temp_word = random.choice(word_list)

    i = 0
    blindex = []
    while i <= (len(temp_word)-1):
       blindex.append("_")
       i += 1
    
    refresh = blindex
    print(" ".join(blindex))
    print(f"Your hangman right now: {HANGMANPICS[0]}")

    def check_letter(lives, trial):
        letter = input("Let's bring it!! what's ur letter guess???")
        for i in range (0, len(blindex)):
            if letter == temp_word[i]:
                blindex[i] = letter
                
            else:
                print("Wrong guess, 1 life taken")
                lives -= 1
                trial += 1
                print(f"Your hangman right now: {HANGMANPICS[trial]}")
                blindex = refresh
                return lives, trial


    while lives != 0:
        check_letter(lives, trial)


            

        

