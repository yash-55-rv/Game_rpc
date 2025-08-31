import random

def play_rock_paper_scissors():
    """Plays a game of rock, paper, scissors."""
    options = ["rock", "paper", "scissors"]
    
    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in options:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    
    # Get computer's choice
    computer_choice = random.choice(options)
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
play_rock_paper_scissors()    #e Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
