# Here is a file attached. You have to perform the following operations of File Handling using Python
# f=open("abc.txt",'r')
# print(f.read())
# f.close()

# f=open("abc.txt",'w')
# f.write('this is a written mode')
# f.write('\nthe contents are now overiding')
# f.close()

f=open('abc.txt', 'a')
f.write('\nFile is open in append mode')
f.write('\nThe contents will not be overridden')
f.close()



f=open("abc.txt",'r')
print(f.read())
f.close()
