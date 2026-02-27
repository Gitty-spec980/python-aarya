# # # Here is a file attached. You have to perform the following operations of File Handling using Python
# # with open('Codingal.txt', 'w') as file:
# #     file.write("Hi. I am SunSunNi and I am 23 years old.")
# # file.close()


# # with open('Codingal.txt', 'r') as file:
# #     data = file.readlines()
# #     print("Words in this file are.......")
# #     for line in data:
# #         word = line.split()
# #         print (word)
# # file.close()
# # Here is a file attached. You have to perform the following operations of File Handling using Python

# new_file = open('New_File.txt', 'x')
# new_file.close()


# import os
# print("Checking if my_file exists or not.....")
# if os.path.exists("my_file.txt"):
#     os.remove("my_file.txt")
# else:
#     print("The file doesnt exist")


# my_file = open("my_file", "w")
# my_file.write("Hi. I am SunSunNi and I am 23 years old.")
# my_file.close()

# os.remove('Codingal.txt')

# Write a Python program to duplicate from one file and then copy it to another file. For copying it in a new file, create a new empty file and upload it in a similar way as you do for the given file.


outputFile = open('UpdatedFile.txt', "w")


inputFile = open('Repeated.txt', "r")

lines_seen_so_far = set()
print("Eliminating duplicate lines....." )

for line in inputFile:

    if line not in lines_seen_so_far:

        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()