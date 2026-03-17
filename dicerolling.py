import random

def roll_dice():
    """
    Simulates rolling a six-sided dice.
    Returns an integer between 1 and 6.
    """
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator.")
    
    while True:
        # Ask the user if they want to roll
        choice = input("\nRoll the dice? (y/n): ").strip().lower()
        
        # Conditional statements to handle user choice
        if choice == 'y':
            result = roll_dice()
            print(f"You rolled a {result}!")
        elif choice == 'n':
            print("Thanks for playing.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Run the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCode is bad. Goodbye.")
