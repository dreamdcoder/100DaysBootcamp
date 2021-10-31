import random

from art import logo, vs
from data import data
import os


def get_item():
    """ Get Item and article associated with it"""
    item = random.choice(data)
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    artcle = 'an' if item['description'].startswith(vowels) else 'a'
    print(item['follower_count'])
    return item, artcle


def format_item(a, article):
    """return formated item details"""
    return f"{a['name']}, {article} {a['description']} ,from {a['country']}."


def compare(a, b):
    """compares follower count of different accounts"""
    if a['follower_count'] > b['follower_count']:
        return 'a'
    elif a['follower_count'] < b['follower_count']:
        return 'b'


# a, article = get_item()
# print(f"Compare A:{a['name']}, {article} {a['description']} ,from {a['country']}.")
# print(vs)
# b, article = get_item()
# print(f"against B:{b['name']}, {article} {b['description']} ,from {b['country']}.")

def game():
    score = 0
    flag = True
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    while flag:
        if score == 0:
            a, a_art = get_item()
        print(f"Compare A:{format_item(a, a_art)}")
        print(vs)

        b, b_art = get_item()
        if a == b:
            b, b_art = get_item()
        print(f"Against B:{format_item(b, b_art)}.")
        guess = input("Who has more followers? 'A' or 'B'.  ").lower()
        answer = compare(a, b)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        if guess == answer:
            a, a_art = b, b_art
            score += 1
            print(f"You are right your current score is:{score}")
        else:
            flag = False
            print(f"Sorry that's wrong your final score is :{score}")


if __name__ == "__main__":
    game()
