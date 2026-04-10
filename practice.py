# #Python Programs to add 2 numbers Take user input
  
# #num1= int(input("Enter the first value."))
# #num2= int(input("Enter the second value"))
# #print("The answer to this equation is", num1+num2)

# l= int(input("Enter the length="))
# w= int(input("Enter the width="))
# print("The answer to the perimeter of this rectangle is", l+w+l+w)
# print("The area of this rectangle is", l*w)




#Write a program to ask the user for their age and print:"Child" if age < 13"Teenager" if 13 ≤ age < 20"Adult" if 20 ≤ age < 60"Senior" if age ≥ 60

age= int(input("Enter your age in this box: "))
if age<13:
    print("You are considered a child in modern day society.")
elif age>=13 and age<20:
    print("You are considered a tennager or adolecent in modern day society.")
elif age>=20 and age<60:
    print("You are considered an adult in modern day society.")
elif age>=60:
    print("You are considered a senior or elderly or millenial or stone age in modern day society.")
else:
    print("Invalid input. ENter a valid one next time.")



