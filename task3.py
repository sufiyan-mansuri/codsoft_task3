# Task 3: Rock, Paper and Scissors game.

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose rock, paper, or scissors (or type 'quit' to exit):")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'quit':
            print("Final Scores - You:", user_score, "Computer:", computer_score)
            break

        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

rock_paper_scissors()
