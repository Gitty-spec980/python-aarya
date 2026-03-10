def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b, handling division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    """Prompt the user for a number and validate input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    
    while True:
        num1 = get_number("Enter first number: ")
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = get_number("Enter second number: ")

        try:
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

    
        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
