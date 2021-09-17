import random

'''
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lst = [rock, paper, scissors]
user_choice = int(input("What do you choose? enter 0 for rock  1 for paper and 2 for scissors \n"))
comp_choice = random.randint(0, 2)
if user_choice > 2 or user_choice < 0:
    print("you entered invalid number")

else:

    print(lst[user_choice])
    print("Computer Chose:")
    print(lst[comp_choice])

    if user_choice == comp_choice:
        print("It's a tie!")
    elif user_choice == 0 and comp_choice == 2:
        print("You Win!")
    elif user_choice == 2 and comp_choice == 0:
        print("You Lose!")
    elif user_choice > comp_choice:
        print("You Win!")
    elif user_choice < comp_choice:
        print("You Lose!")
