import random
from words import word_list
from art import stages,logo


chosen_word = random.choice(word_list)

flag = False

guessed_word = list("-" * len(chosen_word))

word_length = len(chosen_word)

missed = []
player_lives = 6
end_of_game = False
print(logo)

print(chosen_word)
while not end_of_game:
    if "-" not in guessed_word:
        print("Player Wins! Game Over!")
        end_of_game = True
    elif player_lives == 0:
        print("Player Lose! Game Over!")
        end_of_game = True
    else:
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            if guess in guessed_word:
                print(f"You already guessed letter {guess}.")
            else:
                for i in range(word_length):
                    if chosen_word[i] == guess:
                        # print("Right")
                        guessed_word[i] = guess
        else:
            if guess not in missed:
                print(f"You guessed letter {guess},that's not in the word.You lose a life")
                player_lives -= 1
                missed.append(guess)
            else:
                print(f"You already guessed letter {guess}.")
    print(''.join(guessed_word))
    print(stages[player_lives])

