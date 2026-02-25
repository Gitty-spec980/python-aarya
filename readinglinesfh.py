# file = open("readinglinesfh.txt", 'r')
# # print(file.read(15))

# file.close()

# file = open("readinglinesfh.txt", 'a')
# file.write("\n Djibouti Karakas, 13 years old")
# file.close()




# file = open("readinglinesfh.txt", 'r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# Write a Python program to remove lines of a file starting with prefix - Coding and store the contents in a new file.


file = open("readinglinesfh.txt", 'r')
file1 =open("readinglinesfhUpdated.txt", 'w')
for line in file.readlines():
    if not (line.startswith('Coding')):
        print(line)

        file1.write(line)



file1.close()
file.close()