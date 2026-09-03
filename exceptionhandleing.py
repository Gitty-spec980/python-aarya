# # try:
# #     num=int(input("Enter a number- "))
# #     print(num)

# # except ValueError as ve:
# #     print("Exception is", ve)

# try:
#     num=int(input("Enter one number- "))
#     num2=int(input("Enter another number- "))
#     print(num/num2)

# except ZeroDivisionError as zd:
#     print("Exception is a", zd)

# except ValueError as ve:
#     print("Please enter a valid number.")
# except:
#     print("Wrong Input.")
# else:
#     print("No exceptions")
# finally:
#     print("This will execute no matter what.")

valid=False
while not valid:
    try:
        n=int(input("Enter number- "))
        while n%2==0:

            print("Bye.")
        valid = True
    except ValueError:
        print("Invalid")