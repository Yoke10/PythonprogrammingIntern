import random

def print_welcome_message():
    print("Welcome to the Basic Quiz Game!")
    print("You will be asked a series of questions.")
    print("For each question, you will be given 4 options to choose from.")
    print("You will receive points for each correct answer.")
    print("Let's begin!")

def get_questions_and_options():
    questions = [
        {
            "question": " Who developed Python Programming Language?",
            "options": ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
            "correct_answer": "Guido van Rossum"
        },
        {
            "question": "Which of the following is the correct extension of the Python file?",
            "options": [".python", ".pl", ".p", ".py"],
            "correct_answer": ".py"
        },
        {
            "question": "Which keyword is used for function in Python language?",
            "options": ["Function", "def", "Fun", "Define"],
            "correct_answer": "def"
        },
        {
            "question": "Which of the following is used to define a block of code in Python language?",
            "options": ["Indentation", "Key", "Brackets", "All of the mentioned"],
            "correct_answer": "Indentation"
        },
        {
            "question": "Python supports the creation of anonymous functions at runtime, using a construct called",
            "options": ["pi", "anonymous", "lambda", "none of the mentioned"],
            "correct_answer": "lambda"
        },
    ]
    return questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter the number of your answer: ")
    while not user_answer.isdigit() or not 1 <= int(user_answer) <= len(question["options"]):
        print("Invalid input. Please enter a number between 1 and 4.")
        user_answer = input("Enter the number of your answer: ")
    return question["options"][int(user_answer) - 1]

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return 0

def play_game():
    print_welcome_message()
    questions = get_questions_and_options()
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        score += check_answer(user_answer, question["correct_answer"])
    print(f"Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    play_game()