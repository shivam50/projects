print("Hello, Hope you're having a nice day. I'll help you with your bill, just let me know few things ")
size = input("Select your pizza size Small | Medium | Large  ")


if size == "Small":
    print("Small Pizza is $15")
    bill = 15
elif size == "Medium":
    print("Medium Pizza is $20")
    bill = 20
else:
    print("Large pizze is $25")        
    bill = 25
print("Select add ons")
pep = input("Do you want pepperoni? Y/N")
cheese = input("Do youu want chees? Y/N")
if pep == "Y":
    if size == "Small":
        bill += 2
    else:
        bill += 3

if cheese == "Y":
    bill += 1

print(f"total bill is {bill}")