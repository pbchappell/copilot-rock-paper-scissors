#import random
import random

#define main function that handles all the logic
def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'exit' to quit the game.\n")
    
    options = ["rock", "paper", "scissors"]

    while True:
        # User input
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check if the user wants to exit
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        # Validate user input
        if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!\n")
        else:
            print("You lose!\n")


# Run the main function
if __name__ == "__main__":
    main()
