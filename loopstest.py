# # # # Outline:
# # # # Write a program to calculate the sum of whole numbers.

# # # num=int(input("Please enter a valid number- "))

# # # sum=1
# # # for i in range(1, num+1):
# # #     sum=sum*i
# # #     print(sum)

# # # Write a program to reverse the string entered by the user

# # s=input("Enter a word or name here- ")

# # str=''
# # for i in s:
# #     str=i+str
# # print('Reversed string:', str)

# Write a program to print the numbers in reverse order beginning from the number entered by the user.

num=int(input("Enter a number here- "))

for i in range(num,0,-1):
    print(i)