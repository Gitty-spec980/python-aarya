import random

number=random.randint(1, 10)

def intro():
    print("PUT YO DAMN NAME HERE")
    global name
    name = input()
    print(name+",we are going to play a game. I am thinking of a number between 1 and 10")
    if(number%2==0):
        x='even'
    else:x='odd'
    print("\nThis is an {} number".format(x))

    print("GO YA FILTHY ANIMAL!!!!!!!!!! GUEASEEEEEEEE")



def pick():
    guessesTaken = 0

    while guessesTaken < 6:

        enter=input("GUESS.....")
        try:
            guess = int(enter)
            if guess<=10 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<3:
                    if guess<number:
                        print("THE GUESS OF YA DUMB NUMBER WAS TOO LOW")
                    if guess>number:
                        print("THE GUESS OF YA DUMB NUMBER WAS TOO HIGH")

                    if guess !=number:
                        print("YA DUMB FILTHY ANIMAL TRY AGAIN")

                    if guess==number:
                        break

            if guess>10 or guess<1:
                print("YA DUMB FILTHY ANIMAL THAT NUMBER ISNT IN THE RANGE")

                print("pleASE ENtER A numBER BEtween 1 anD 1cptone0")

        except:
            print("I DONT THINK THAT ",enter," is a number. sorry.....SIKEEEEE")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('wow..good job {}. You guesses my number in {} guesses'.format(name, guessesTaken))

    if guess !=number:
        print('no. the number i was thinking of was' + str(number))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes" or playagain=="YES":
    intro()
    pick()
    print("Do you wanna play again?")
    playagain=input()