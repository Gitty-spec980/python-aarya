print("Welcome to the Holiday planner.")


print("What holiday would you like to go to? Summer vacation or winter vacation.")

desicion= int(input("Enter 1 or 2."))
print()

if desicion== 1:
    print("What activity would you like?")
    print("Hiking (1) or Snorkeling (2)")

    print()

    summer_des=int(input("Enter 1 or 2"))
    print()

    if summer_des==1:
        print("You picked hiking (1.)")
    else:
        print("You picked snorkeling (2.)")

elif desicion == 2:
    print("What activity would you like to choso, skiing (1) or hot chocolate bar? (2).")

winter_des= int(input("Enter 1 or 2."))
print()

if winter_des==1:
        print("You chose skiing.")
else:
        print("You chose hot chocolate bar.")

        

