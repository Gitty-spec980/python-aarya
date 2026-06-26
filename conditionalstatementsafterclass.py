# Python Program: Grading System using Conditional Statements

def get_grade(score):
    """
    Returns the grade based on the score.
    Uses if-elif-else conditional statements.
    """
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def main():
    try:
        # Take input from the user
        score_input = input("Enter your score (0-100): ").strip()

        # Validate if input is a number
        if not score_input.isdigit():
            print("Invalid input. Please enter a number between 0 and 100.")
            return

        score = int(score_input)

        # Validate score range
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return

        # Get and display the grade
        grade = get_grade(score)
        print(f" Your grade is: {grade}")

        # Additional feedback using conditional statements
        if grade == "A+":
            print(" Excellent work! Keep it up!")
        elif grade in ["A", "B"]:
            print(" Good job! You can aim even higher.")
        elif grade in ["C", "D"]:
            print(" You passed, but there's room for improvement.")
        else:
            print(" Don't give up. Study harder next time.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
