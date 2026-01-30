# Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.


class Rectangle:

    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        print("Length of the rectangle is,", self.length)
        print("Width of rectangle is,", self.width)
        print("The area of the rectangle is,", self.length*self.width)

ob1=Rectangle(13,36)

ob1.area()
    

        