import  random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'attempts', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_syms = int(input("How many symbols would you like?\n"))
nr_nums = int(input("How many numbers would you like?\n"))
pwd = ''

for i in range(nr_letters):
    pwd += random.choice(letters)
for j in range(nr_syms):
    pwd += random.choice(symbols)
for k in range(nr_nums):
    pwd += random.choice(numbers)

x = list(pwd)
random.shuffle(x)
print()
x
print(f"here is your password :{''.join(x)}")

