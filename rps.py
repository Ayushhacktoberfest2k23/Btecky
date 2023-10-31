import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    
    # User's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    # Computer's choice
    computer_choice = random.choice(choices)
    
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
play_game()
