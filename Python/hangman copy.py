import random


start = input("Wanna Play Hangman!!! Press 1 to start")

if start == "1":
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
    wordlist = ["Hello", "camel", "Ramen", "Samurai" ]
    lives = 6
    trials = 0
    game_over = False




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

    #1. Randomly choose a word from wordlist and assign it to var choosen_word

    choosen_word = random.choice(wordlist).lower()


    #4. Create a placeholder with same no of blanks as choosen_word
    blanks = ["_"]*len(choosen_word)

    found = False

    #3. check if guess is one of the letter in choosen_word. Print right if true, wrong if false
    #5. Create a display that puts the right letter in the blank

    #Game Logic
    def guess_check(guess):
        global found
        found = False   

        for i in range(len(choosen_word)):
            if choosen_word[i] == guess:
                found = True
                blanks[i] = guess
                    
        return found




    while lives > 0 and '_' in blanks:
        guess = input("guess a letter").lower()

        if guess_check(guess):
            print("Right guess")
        else:
            print("Wrong guess")
            lives -= 1
            trials += 1
            print(f" Your Hangman is now : {HANGMANPICS[trials]}")

        print(" ".join(blanks))


    #game won or lost
    if "_" not in blanks:
        print("Yay you won")
    else:
        print("Hangman is Dead!!!! You Lost")
        game_over = True










