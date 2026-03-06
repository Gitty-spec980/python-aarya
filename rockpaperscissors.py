import random
print("Welcome to the Rock Paper Scissor game./n")
player_wins = 0
computer_wins = 0
while True:
    player = input("Enter rock, paper, or scissors.").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer}.")
    if player == computer:
        print("It is a tie. Both opponents chose {player},.")
    elif player == "rock":
        if computer == "scissors":
            print("Rock defeats scissors. Player wins.")
            player_wins+=1
        else:
            print("Paper covers rock. You lose.")
            computer_wins+=1
    elif player == "scissors":
        if computer == "paper":
             print("Scissors cuts paper. You win.")
             player_wins+=1
        else:
            print("Rock smashes scissors. You lose")
            computer_wins+=1
    print("You have "+str(player_wins)+" wins")
    print("The computer has "+str(computer_wins)+" wins")


    repeat = input("\nPlay again? Yes or No?")
    if repeat.lower() !="Yes":
        print("Thank you for playing with us dear player. We hope you have a wonderful day.")
        break

