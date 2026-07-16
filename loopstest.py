# # # # # Outline:
# # # # # Write a program to calculate the sum of whole numbers.

# # # # num=int(input("Please enter a valid number- "))

# # # # sum=1
# # # # for i in range(1, num+1):
# # # #     sum=sum*i
# # # #     print(sum)

# # # # Write a program to reverse the string entered by the user

# # # s=input("Enter a word or name here- ")

# # # str=''
# # # for i in s:
# # #     str=i+str
# # # print('Reversed string:', str)

# # Write a program to print the numbers in reverse order beginning from the number entered by the user.

# num=int(input("Enter a number here- "))

# for i in range(num,0,-1):
#     print(i)


chores= ["Make your bed", "Do your Laundry", "Take out the Trash", "Help with dinner", "DO NOT FIGHT WITH ANJUUUUU"]


original_count= len(chores)

print("You have", original_count, "chores to finish today.")

completed_count=0

while len(chores)>0:
    next_chore=chores[0]
    answer=input("Have you finished- " +next_chore+ "? Yes or No- ")

    if answer == "Yes":
        chores.pop(0)
        completed_count = completed_count+1
        print("Nice. Chore completed.")
    else:
        print("Well, what are you doing? Finish it, then check again.")

    print("Chores Remaining- ", len(chores))
    print("")
print("All of your chores are done. Good job.")

print("")
print("Let us look at what an infinite loop is like- ")
test_value = 0
saftey_counter = 0
while test_value<=0:
    print("This comdition never changes. This infinite loop would run forever.")
    saftey_counter +=1
    if saftey_counter == 3:
        print("(Stopping here on purpose. A real infinite loop would never stop running and would go on FOREVER.)")
        break





print("")
print("*************Chore Checklist Summary*************")
print("Chores assigned today- ", original_count)
print("Chores completed today- ", completed_count)
print("Chores remaining- ", len(chores))
print("***************************************")














