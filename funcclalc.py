
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
print("funk calculator hehehehe")

try:
    a = float(input("First number- "))
    b = float(input("Second number- "))
    op = input("Operation (add, subtract, multiply, divide): ")

    if op == "add":
        print("Result:", add(a, b))
    elif op == "subtract":
        print("Result:", subtract(a, b))
    elif op == "multiply":
        print("Result:", multiply(a, b))
    elif op == "divide":
        print("Result:", divide(a, b))
    else:
        print("Unknown operation.")
except ValueError:
    print("Numbers only. Are you dumb?")
except ZeroDivisionError:
    print("You cannot divide by zero. Dummy.")
finally:
    print("Thanks for using the calculator. I gues...")
