import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_lett = int(input("How many letters would you like in your password?"))
nr_symb = int(input("How many symbols would you like?"))
nr_num = int(input("How many numbers would you like?"))

pass_list = []

list1 = [letters, symbols, numbers]

for i in range(0, nr_lett):
   # pass_list.append(letters[random.randint(0,len(letters)-1)])
    pass_list.append(random.choice(letters))


for i in range(0, nr_symb):
    pass_list.append(random.choice(symbols))

for i in range(0, nr_num):
    pass_list.append(random.choice(numbers))

random.shuffle(pass_list)


password = ""

for i in range(0, len(pass_list)-1):
     password += pass_list[i]

print(password)