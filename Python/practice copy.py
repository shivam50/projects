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

def display_intro():
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


if start == 1:
    
    lives = 6
    trial = 0

def get_word():
    word_list = ["babuna", "timki", "kantan", "Chotababu", "Gattabaabu"]
    temp_word = random.choice(word_list).lower()
    return temp_word


def initialize_blanks(word):
    return ["_" for _ in word]

def display_status(blanks, trial):
    print("\n" + " ".join(blanks))
    print(HANGMANPICS[trial])
    
def get_guess():
    return input("Enter your guess (a single letter): ").lower()


def update_blanks(word, blanks, guess):
    found = False
    for i in range(len(word)):
        if word[i] == guess:
            blanks[i] = guess
            found = True
            
def Play_game():
    word = get_word()
    blanks = initialize_blanks(word)
    lives = len(HANGMANPICS) - 1
    trial = 0

    while trial < lives and "_" in blanks:
        display_status(blanks, trial)
        guess = get_guess()

        if update_blanks(word, blanks, guess):
            print("Nice, you guessed a letter")
        else:
            trial += 1
            print("OOPS, Wrong guess")

    display_status(blanks, trial)

    if "_" not in blanks:
        print("\n🎉 You saved the hangman! The word was:", word)
    else:
        print("\n💀 You lost! The word was:", word)


# Start the game
start = input("Let's Play Hangman! Press 1 to begin: ")
if start == '1':
    display_intro()
    Play_game()
else:
    print("Maybe next time!")

    