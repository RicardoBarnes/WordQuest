import random
import sys

choices = {"r": "rock", "p": "paper", "s": "scissors"}

Wanna_play = input("Would you like to play Rock, Paper, Scissors? Enter N for no and Y for yes ").lower()

if Wanna_play == "n":
    print("Come again next time!")
    sys.exit()

score = {"user": 0, "computer": 0}

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def display_choice_art(choice):
    if choice == "r":
        print(rock_art)
    elif choice == "p":
        print(paper_art)
    elif choice == "s":
        print(scissors_art)

while True:
    option = input("Choose R for Rock, P for paper, and S for Scissors ").lower()

    if option not in choices:
        print("Invalid input. Please choose R, P, or S.")
        continue

    computerChoice = random.choice(list(choices.keys()))

    user_choice = choices[option]
    computer_choice = choices[computerChoice]

    print(f"\nYou chose {user_choice}:")
    display_choice_art(option)

    print(f"\nThe computer chose {computer_choice}:")
    display_choice_art(computerChoice)

    if option == computerChoice:
        print("It's a tie!")
    elif (option == "r" and computerChoice == "s") or (option == "p" and computerChoice == "r") or (
            option == "s" and computerChoice == "p"):
        print(f"You win! {user_choice.capitalize()} beats {computer_choice}")
        score["user"] += 1
    else:
        print(f"Computer wins! {computer_choice.capitalize()} beats {user_choice}")
        score["computer"] += 1

    play_again = input("\nDo you want to play again? (Y/N) ").lower()
    if play_again != "y":
        break

print("\nFinal Score:")
print(f"You: {score['user']}")
print(f"Computer: {score['computer']}")
