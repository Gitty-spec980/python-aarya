#Build a game where the computer picks a secret number between 1 and 50. You have 5 attempts to guess it. After every wrong guess your program shows a hint telling you how close you are. Remaining lives are shown as hearts after each attempt
num=int(input("Enter a number 1-50 here- "))
attempts = 5
while attempts>0:
    guess=int(input("Enter your guess- "))
    if guess==num:
        print("Nice job. you got the correct answer.")
    difference=guess-num