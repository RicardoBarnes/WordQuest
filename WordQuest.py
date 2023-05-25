def word_quest():
    print("Welcome to Word Quest!")
    print("Let your word choices guide you on an exciting adventure.")

    points = 1

    # Scenario 1
    print("\nScenario 1:")
    print("You find yourself standing at a crossroad in a dense forest.")
    print("The path to the left is covered in moss and seems mysterious, while the path to the right is well-trodden and familiar.")

    print("\nWord Choice:")
    print("A: Adventure")
    print("B: Familiarity")

    choice = input("Which word do you choose? (Type 'A' or 'B'): ")

    if choice.upper() == 'A':
        print("\nYou choose adventure!")
        points += 5

        # Scenario 2
        print("\nScenario 2:")
        print("Mesmerized by the beauty of the waterfall, you notice a small wooden bridge spanning across a nearby river.")
        print("On the other side of the bridge, you glimpse a hidden cave entrance partially concealed by vines.")

        print("\nWord Choice:")
        print("A: Explore")
        print("B: Retreat")

        choice = input("Which word do you choose? (Type 'A' or 'B'): ")

        if choice.upper() == 'A':
            print("\nYou choose to explore!")
            points += 10
            print("\nCongratulations! You've discovered a treasure chest at the heart of the cave.")
            print("Your total points: ", points)
        elif choice.upper() == 'B':
            print("\nYou choose to retreat.")
            points -= 5
            print("\nWhile you miss out on the hidden treasures, you manage to find your way back to safety.")
            print("Your total points: ", points)
        else:
            print("\nInvalid choice. Game over!")
            return

    elif choice.upper() == 'B':
        print("\nYou choose familiarity!")
        points -= 3
        print("\nYou follow the familiar path, but it leads you to a dead end.")
        print("Your total points: ", points)
    else:
        print("\nInvalid choice. Game over!")
        return

    print("\nThank you for playing Word Quest!")


# Start the game

word_quest()
