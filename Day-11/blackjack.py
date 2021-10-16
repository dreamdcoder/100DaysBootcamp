import random
import os

from bj_art import logo
from replit import clear


def draw(user_total, user_cards):
    """Return Random card and its value from cards deck"""
    cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    card, value = random.choice(list(cards.items()))
    user_cards.append(card)
    user_total += value
    return user_total, user_cards


def check_score(score, comp_cards):
    if score > 21 and 'A' in comp_cards:
        score -= 10
    elif score == 21 and 'A' in comp_cards:
        score = 0
    return score


def compare(user_score, computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


choice = input("Do you want to play black jack 'y' or 'n'?. ")
while choice == 'y':
    print(logo)
    user_cards = []
    comp_cards = []
    user_total = 0
    comp_total = 0
    for _ in range(2):
        user_total, user_cards = draw(user_total, user_cards)
    print(f"Your Cards are {user_cards} and your total is {user_total}.")
    comp_total, comp_cards = draw(comp_total, comp_cards)
    print(f"Computer's cards are {comp_cards} and computer total is {comp_total}.")
    should_continue = input("Press 'y', if you want to draw the card or 'n' to pass.  ")
    while should_continue == 'y':
        user_total, user_cards = draw(user_total, user_cards)

        print(f"Your Cards are {user_cards} and your total is {user_total}.")
        should_continue = input("Press 'y', if you want to draw the card or 'n' to pass.  ")

    if user_total > 21:
        comp_total, comp_cards = draw(comp_total, comp_cards)
    else:
        while comp_total < 17:
            user_total = check_score(user_total, user_cards)
            comp_total, comp_cards = draw(comp_total, comp_cards)

    print(f"Your final hand is {user_cards} and final total is {user_total}.")
    print(f"Computer's final hand is {comp_cards} and final total is {comp_total}.")
    print(compare(user_total, comp_total))
    choice = input("Do you want to play black jack 'y' or 'n'?. ")
    os.system('cls' if os.name == 'nt' else 'clear')
