from art import logo

# TODO : 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


#variables

milk = 1000
water = 1000
coffee = 1000
money = 0





#functions 

def checkMoney():
    coins = {}
    values = {'dimes': 0.10, 'quarters': 0.25, 'nickels': 0.05, 'pennies': 0.01}
    total = 0
    repeat = True
    coin_types = ['dimes','nickels','pennies','quarters']
    for coin in coin_types:
        coins[coin] = int(input(f"Enter amount of {coin}"))

    print(coins)
    for coin, count in coins.items():
        total += values[coin] * count
    print(total)
    return total
                
    



def espresso(milk, water, coffee, money):
    cost = 2.85
    if water > 200 and coffee > 20:
        total = checkMoney()
        if total > cost : 
            print("Here is ur espresso")


    else:
        if water < 200:
            print("Sorry, there isnt enough water")
        
        if coffee < 20:
            print("Sorry, not enough coffee")


    
def latte(milk, water, coffee, money):
    cost = 3.40
    if water > 100 and coffee > 20 and milk > 100:
        total = checkMoney()
        if total > cost : 
            print("Here is ur latte")


    else:
        if water < 200:
            print("Sorry, there isnt enough water")
        
        if coffee < 20:
            print("Sorry, not enough coffee")
        
        if milk < 100:
            print("Sorry, not enough milk")



def cappuccino(milk, water, coffee, money):
    cost = 3.65
    if water > 200 and coffee > 20 and milk > 50:
        total = checkMoney()
        if total > cost : 
            print("Here is ur cappucino")


    else:
        if water < 200:
            print("Sorry, there isnt enough water")
        
        if coffee < 20:
            print("Sorry, not enough coffee")

        if milk < 50:
            print("Sorry, not enough milk")





choice = input("What would you like? (espresso: press e /latte: press l /cappuccino: press c ):")
if choice == "e":
    espresso(milk, water, coffee, money)
    coffee -= 20
    water -= 100
    print(f"coffee left is {coffee}")
elif choice == "l":
    latte(milk, water, coffee, money)
    coffee -= 20
    water -= 100
    milk -= 100
    print(f"coffee left is {coffee}")
elif choice == "c":
    cappuccino(milk, water, coffee, money)
    coffee -= 20
    water -= 100
    milk -= 50
    print(f"coffee left is {coffee}")
else:
    print("wronhg inp")











''' 
Coffee Machine Program Requirements
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
'''


