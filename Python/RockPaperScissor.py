from ast import Continue
import random

def rps():
    print("Hi, Lets play Rock Paper Scissorss")
    cchoice = random.randint(0,2)

    rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    paper = """
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    scissor = """
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """

    choice = input("Select rock paper or scissors    ").strip().lower()
    if choice == "rock":
        print(rock)
        uchoice = 0
    elif choice == "paper":
        print(paper)
        uchoice = 1
    else:
        print(scissor)
        uchoice = 2
        
    if cchoice == 0:
        print(f"Computer has selected {rock}")
        if uchoice == 0:
            print("Draw, lets play again")
            again = input("Do u wanna play again? y/n").strip().lower()
            if again == "y":
                rps()
            else:
                print("Thanks for Playing")
        elif uchoice == 1:
            print("Timki Win")
        else:
            print("Computer Wins")
        
    if cchoice == 1:
        print(f"Computer has selected {paper}")
        if uchoice == 0:
            print("Computer Wins")
        elif uchoice == 1:
            print("Draw, Lets play again")
            again = input("Do u wanna play again? y/n").strip().lower()
            if again == "y":
                rps()
            else:
                print("Thanks for Playing")
        else:
            print("You Wins")
        
    if cchoice == 2:
        print(f"Computer has selected {scissor}")
        if uchoice == 0:
            print("Computer Wins")
        elif uchoice == 1:
            print("You Win")
        else:
            print("Draw, Lets play again")
            again = input("Do u wanna play again? y/n").strip().lower()
            if again == "y":
                rps()
            else:
                print("Thanks for Playing")

rps()
        



