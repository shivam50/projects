import random

numb = int(random.randint(0,100))

#print(f"Psst ur no is {numb}")

attempts = 5

won = False

def user_attempt(attempts, won):
    att = int(input("Guess a no"))
    if att == numb:
        print("you won")
        won = True
    elif att < numb:
        attempts -= 1
        print(f"go higher, attempts remaining {attempts}")
    elif att > numb:
        attempts -= 1
        print(f"go lower, attempts remaining {attempts}")

    return attempts, won

while attempts >= 0 and not won:
    attempts, won = user_attempt(attempts, won)
    if attempts == 0:
        print("you loose")
    

if not won:
    print(f"😢 You lose. The number was {numb}")