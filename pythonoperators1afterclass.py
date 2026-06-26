def get_positive_number():
    while True:
        try:
            num = float(input("Enter a number: "))
            if num < 0:
                print(" Square root for this number is not real. Try again.")
            else:
                return num
        except ValueError:
            print(" Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    number = get_positive_number()

    
    square_root = number ** 0.5

print(" The square root of",number "is",square_root)
