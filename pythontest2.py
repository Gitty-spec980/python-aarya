import math

def add(a,b):
    a= 12
    b=3
    print(a+b)
    sum= add(a,b)
    print("Sum is- ", sum)

def sub(a,b):
    print(a-b)
    difference=a-b
    print("Difference is- ", difference)

def mult(a,b):
    print(a*b)
    product=a*b
    print("Product is- ", product)

def div(a,b):
    print(a/b)
    quotient=a/b
    print("Quotient is- ", quotient)

    return math


try:
   a,b= input("Here are the resluts,")
   print(a,b)
except ValueError:
    print("Invalid. Enter a number.")
except ZeroDivisionError:
    print("You cannot divide a zero.")





