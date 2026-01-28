# # # Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.

# # class Parrot:

# #     # class attribute
# #     species = "bird"

# #     # instance attribute
# #     def __init__(self, name, age):
# #         self.name=name
# #         self.age=age

# # ob1 = Parrot("Sally", 25)
# # ob2 = Parrot("Polly", 1005)


# # print("Sally is a {}".format(ob1.species))
# # print("Polly is also a {}".format(ob2.species))


# # print("{} is {} years old".format(ob1.name, ob1.age))
# # print("{} is {} years old".format(ob2.name, ob2.age))


# Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instance methods for this class named sing and dance, making them print a message. Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.




class Parrot:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
ob1 = Parrot("Bae", 10)


print(ob1.sing("'Blue Valentine"))
print(ob1.dance())










