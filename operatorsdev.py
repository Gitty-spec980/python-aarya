# # # # # # # There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?
# # # # # # tr1=98
# # # # # # tr2=94
# # # # # # tr3=41
# # # # # # tr4=96
# # # # # # tr5=11
# # # # # # answer=(tr1+tr2+tr3+tr4+tr5)/5
# # # # # # print("the average height of the trees is ", answer)

# # # # # Write a program to calculate the number of notes in the given amount?

# # # # amt = int(input("Enter amount"))
# # # # usd100=amt // 100
# # # # amt = amt%100

# # # # usd50=amt // 50
# # # # amt = amt%50

# # # # usd10=amt // 10
# # # # amt = amt%10

# # # # usd5=amt // 5
# # # # amt = amt%5

# # # # usd1=amt // 1


# # # # print("Notes of 100:", usd100)
# # # # print("Notes of 5:", usd50)
# # # # print("Notes of 10:", usd10)
# # # # print("Notes of 5:", usd5)
# # # # print("Notes of 1:", usd1)

# # # a = 123
# # # b = 3
# # # c = -10

# # # if a and b and c:
# # #     print("All values are True")
# # # else:
# # #     print("At least one value is false.")

# # # a=10
# # # b=-10
# # # c=0

# # # if a>0 or b>0:
# # #     print("Either of the number is greater than 0")
# # # else:
# # #     print("No number is greater than 0")

# # # if b>0 or c >0:
# # #     print("Either of the number is greater than 0")
# # # else:
# # #     print("No number is greater than 0")

# a = 10
# b = 12
# c = 12


# print(not(a == b))


# print(not(b == c))

# a = "python"
# b = "coding"


# if not (a == b):
#     print(a, 'and', b, 'are different.')

#     a = 4
#     b = 5


# if not ((a==1)) == ((b == 5)):
#     print('Hello WeRLd')


# a = int(input("Enter a number: "))

# if not (a % 2 == 0):
#     print(a, "Is an odd number...........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................")





















height = float(input("Enter your height in inches- "))
weight = float(input("Enter your weight in - lbs"))

bmi = (weight / (height**2))*703

print("BMI =", round(bmi, 1))

if bmi<18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")