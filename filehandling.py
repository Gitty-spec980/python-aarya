# # Here is a file attached. You have to perform the following operations of File Handling using Python
# # f=open("abc.txt",'r')
# # print(f.read())
# # f.close()

# # f=open("abc.txt",'w')
# # f.write('this is a written mode')
# # f.write('\nthe contents are now overiding')
# # f.close()

# f=open('abc.txt', 'a')
# f.write('\nFile is open in append mode')
# f.write('\nThe contents will not be overridden')
# f.close()



# f=open("abc.txt",'r')
# print(f.read())
# f.close()
# Write a Python program that can calculate and return the total number of lines present inside a file. First, you would be required to read the contents of the file.

file = open("abc.txt", "r")
Counter = 0



f = file.read()
CoList = f.split("\n")

for i in CoList:
    if i:
        Counter += 1
print("This is the # of lines in the file")
print(Counter)
