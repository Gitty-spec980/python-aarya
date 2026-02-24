
student_data = {
    "Jamal": (20, "Streaming"),
    "IShowSpeed": (22, "Streaming"),
    "Fanum": (34, "Admit to eating KFC EVERYDAY.")
}


key = input("Enter the student's name: ").strip()


if key in student_data:
    
    age, major = student_data[key]
    print(f" Found: {key} is {age} years old and does {major}.")
else:
    print(" Key not found in the dictionary.")
