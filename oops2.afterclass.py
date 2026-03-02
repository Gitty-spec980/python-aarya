class square:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("The length of the square is ", self.length)
        print("The width of the square is ", self.width)
        print("The area of the square is ", self.length*self.width)

ob1=square(67,67)
ob1.area()