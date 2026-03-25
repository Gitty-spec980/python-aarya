# Simple Python Quiz Program

def run_quiz(questions):
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        # Input validation loop
        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid choice. Please enter A, B, C, or D.")

        if answer == q["answer"]:
            print(" Correct.")
            score += 1
        else:
            print(f" Wrong.The correct answer was {q['answer']}.")

    print(f"\nYour final score: {score}/{len(questions)}")


if __name__ == "__main__":
    # List of quiz questions
    quiz_questions = [
        {
            "question": "1. What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "2. Which language is this quiz written in?",
            "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
            "answer": "B"
        },
        {
            "question": "3. What is 5 + 3?",
            "options": ["A. 6", "B. 8", "C. 9", "D. 7"],
            "answer": "B"
        }
    ]

    print("=== Welcome to the Python Quiz ===")
    run_quiz(quiz_questions)
