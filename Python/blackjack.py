import random

print("Let us play a blackjack game, press 'y' to start")

card_deck = {
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 10
}

player_cards = []

comp_cards = []

#game-logic

for i in {0,1}:
    player_cards.append(random.choice(list(card_deck)))
    comp_cards.append(random.choice(list(card_deck)))


print(f"player hand is {player_cards} ")

print(f"computer hand is [{comp_cards[0]}, 'X'] ")



total_player = sum(card_deck[card] for card in player_cards)
total_comp = sum(card_deck[card] for card in comp_cards)


while total_player <= 21:
    choice = input("Hit or pass?? press 'y' for hit and 'n' to pass \n")
    if choice == 'y':
        player_cards.append(random.choice(list(card_deck)))
        print(f"player hand is {player_cards} ")
        total_player = sum(card_deck[card] for card in player_cards)
    else:
        break



print("Time to check who wins")
print(f"comp sum is {total_comp} plaer sum is {total_player}")


if total_player > 21 :
    print(f"Player busts with {total_player}. You lose.")
else:
    total_comp = sum(card_deck[card] for card in comp_cards)
    while total_comp < 17:
        comp_cards.append(random.choice(list(card_deck)))
        total_comp = sum(card_deck[card] for card in comp_cards)
   
    print(f"Computer hand is: {comp_cards}, total: {total_comp}")
    print(f"Player total: {total_player}")

    # decide winner
    if total_comp > 21 or total_player > total_comp:
        print("You win!")
    elif total_player < total_comp:
        print("Computer wins!")
    else:
        print("It's a draw!")


        




