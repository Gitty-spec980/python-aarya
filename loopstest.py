# Outline:
# Write a program to calculate the sum of whole numbers.

num=int(input("Please enter a valid number- "))

sum=1
for i in range(1, num+1):
    sum=sum*i
    print(sum)
