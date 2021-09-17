print("Welcome to Yogi's Pizzeria!")
size = input("What size pizza do you want? S,M or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheeeeeese ? Y or N ").upper()

bill = 0

if size == 'S':
    bill += 15

elif size == 'M':
    bill += 20

else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is ${bill}.")


