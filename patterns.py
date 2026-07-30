# # #Right Angle Triangle

# # rows=int(input("Enter the amount of rows you want- "))
# # for i in range(1,rows+1):
# #     for j in range(i):
# #         print("*", end=" ")
# #     print()
# #Floyds triangle

# rows = int(input("ENter the amount of rows you want- "))
# num=1
# for i in range(num,rows+1):
#     for j in range(i):
#        print(num, end=" ")
#        num+=1
#     print() 


rowsize = int(input("Enter the amount of rows you want- "))
if rowsize%2==0:
    halfdiamrow = int(rowsize/2)
else:
    halfdiamrow = int(rowsize/2)+1
space = halfdiamrow-1

for i in range(1, halfdiamrow+1):
    for j in range(1, space+1):

        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))

        num = num+1
    print()
space = 1

for i in range(1, halfdiamrow):
    for j in range(1, space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1,2*(halfdiamrow-i)):
        print(end=str(num))

        num= num+1
    print()