#Am online learing platforn randomly selects questions for students
import random

questions = [
    "What is a Python module?",
    "What is a Python package?",
    "What is recursion?",
    "What is a lambda function?",
    "What is a dictionary?",
    "What is inheritance?",
    "What is polymorphism?",
    "What is exception handling?",
    "What is file handling?",
    "What is a constructor?"
]

question = random.choice(questions)

print("------ Python Quiz ------")
print("Question:")
print(question)

answer = input("\nEnter your answer: ")

print("Your answer is:", answer)
print("Answer recorded successfully!")