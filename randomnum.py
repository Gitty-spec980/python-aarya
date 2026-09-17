# # import random
# # playing=True
# # number=str(random.randint(0,9))


# # print("The computer will generate a number from 0-9. Guess one digit at a time. Choos wisely.")
# # print("The game ends when you get the answer right. Good luck.")

# # while playing:
# #     guess=input("Pick a digit.")
# #     if number==guess:
# #         print("Well done.")
# #         print("The number was", number)
# #         break

# #     else:
# #         print("Your guess is not right. Tch. Choose wisely.")

# import random
# while True:
#     user_action=input("Enter a choice. Rock, paper, or scissors.")
#     possible_actions=["rock", "paper", "scissors"]
#     computer_action=random.choice(possible_actions)
#     print(f"\nYou chose {user_action}. The program chose {computer_action}.\n")


#     if user_action==computer_action:
#         print(f"Tie.")

#     elif user_action == "rock":
#         if computer_action== "scissors":
#             print("You win.")
#         else:
#             print("You lost.")

#     elif user_action =="paper":
#         if computer_action== "rock":
#             print("You win.")
#         else:
#             print("You lost.")
#     elif user_action=="scissors":
#         if computer_action== "paper":
#             print("You win.")
#         else:
#             print("You lost.")
#     play_again= input("Play again? y/n- ")
#     if play_again !="y":
#         break

import math
print(math.ceil(24.8))
print(math.sqrt(24))
print(math.floor(19.3))
print(math.pow(4,3))
print(math.fabs(-5))
print(math.cbrt(64))
print(math.gcd(12,24))
print(math.factorial(5))