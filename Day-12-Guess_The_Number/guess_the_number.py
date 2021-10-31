import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    """Sets  difficulty level for game"""
    difficulty = input("Choose a difficulty. 'easy' or 'hard': ").lower()
    attempts = 0
    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    else:
        print("Enter valid values.")
    return attempts


def check_answer(guess, chosen_number):
    """compares guessed number and chosen number and returns boolean"""
    if guess == chosen_number:
        print("You have guessed it correct!")
        return True
    elif guess > chosen_number:
        print("Too high.\nGuess again.")
    elif guess < chosen_number:
        print("Too low.\nGuess again.")
    return False


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)
    print(f"Chosen Number is {chosen_number}")
    Flag = False

    attempts = set_difficulty()
    while attempts > 0 and not Flag:
        print(f"You have {attempts} attempt(s) remaining to guess the number.")
        guess = int(input("Make a guess: "))
        Flag = check_answer(guess, chosen_number)
        attempts -= 1

    if not Flag:
        print("You ran out of attempts!")


if __name__ == "__main__":
    game()
