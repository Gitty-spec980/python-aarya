# # Write a program to create patterns with stars using loops in Python.
# print("Star Pattern \n")
# for i in range(1,6):
#     for j in range(i):
#         print(":)", end=" ")
#     print('\n')


# print("Inverted Star Pattern")
# for i in range(6,1, -1):
#     for j in range(i, 1, -1):
#         print(":)", end=" ")
#     print('\n')

def no_notes(a):
    Q = [2000, 500, 20, 100, 50, 20, 10]
    x = 0
    for i in range(7):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q

amount = int(input("Enter Total Amount"))
no_notes(amount)