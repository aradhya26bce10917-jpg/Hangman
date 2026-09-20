import random

from hangman_words import word_list
from hangman_art import stages, logo
from player import Player
from game_logic import create_placeholder, update_display, check_guess, word_completed


print(logo)

name = input("Enter your name: ")
player = Player(name)

chosen_word = random.choice(word_list)
display = create_placeholder(chosen_word)

print("Word to guess: " + display)

game_over = False

while not game_over:

    print(f"\n{player.name}, you have {player.lives}/6 lives left.")
    print("Guessed letters:", player.guessed_letters)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    if guess in player.guessed_letters:
        print(f"You've already guessed {guess}.")
        continue

    player.add_guess(guess)

    if check_guess(chosen_word, guess):
        print(f"Good guess! {guess} is in the word.")
        player.add_score()
    else:
        print(f"You guessed {guess}, that's not in the word.")
        player.lose_life()

    display = update_display(chosen_word, player.guessed_letters)

    print("Word to guess: " + display)
    print(stages[player.lives])

    if word_completed(display):
        game_over = True
        print("\n****************************")
        print(f"YOU WIN, {player.name}!")
        print(f"Score: {player.score}")
        print("****************************")

    elif player.lives == 0:
        game_over = True
        print("\n****************************")
        print(f"IT WAS {chosen_word}!")
        print("YOU LOSE!")
        print("****************************")