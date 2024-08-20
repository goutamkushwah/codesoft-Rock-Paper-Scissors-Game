import random

cPoints = 0
pPoints = 0

def get_player_choice():
    """Get player's choice."""
    choices = ('r', 'p', 's')
    while True:
        symbol = input("Choose rock(r), paper(p), or scissors(s): ").lower()
        if symbol in choices:
            return symbol
        print("Invalid option. Please enter a valid choice.")

def get_computer_choice():
    """Get computer's choice."""
    choices = ('r', 'p', 's')
    return random.choice(choices)

def play_round():
    """Play a single round of the game."""
    global cPoints, pPoints
    pChoice = get_player_choice()
    cChoice = get_computer_choice()
    print("The computer has chosen", cChoice)
    print("You chose", pChoice)
    if pChoice == cChoice:
        print("It's a tie! No one gets a point.")
    elif (pChoice == "r" and cChoice == "s") or (pChoice == "s" and cChoice == "p") or (pChoice == "p" and cChoice == "r"):
        print("You won!")
        pPoints += 1
    else:
        print("Aww. I won.")
        cPoints += 1
    print()

def main():
    """Main function to play the game."""
    global cPoints, pPoints
    print("Welcome to Rock Paper and Scissors game!!!")
    while True:
        for _ in range(5):
            play_round()
        print("Good job!\nYour score is:", pPoints, "\nMy score is", cPoints)
        print()
        try:
            again = int(input("Press 1 to continue, 2 to reset and continue, 3 to exit: "))
            if again == 1:
                continue
            elif again == 2:
                pPoints = 0
                cPoints = 0
                continue
            elif again == 3:
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
