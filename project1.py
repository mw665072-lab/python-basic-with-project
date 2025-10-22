import random
developer_qna = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its readability and versatility.",
    "What is React?": "React is a JavaScript library for building user interfaces, maintained by Facebook.",
    "What is Node.js?": "Node.js is a runtime environment that allows you to run JavaScript on the server side.",
    "What is Git?": "Git is a distributed version control system used to track changes in source code.",
    "What is an API?": "An API (Application Programming Interface) is a set of rules that allow different software applications to communicate.",
    "What is a database?": "A database is an organized collection of structured information.",
    "What is REST API?": "REST API is an architectural style for designing networked applications using HTTP requests.",
    "What is Docker?": "Docker is a platform that allows developers to automate the deployment of applications inside lightweight containers.",
    "What is CI/CD?": "CI/CD stands.",
    "What is Agile?": "Agile is a project management methodology that promotes iterative development and collaboration."
}

def project_score_calculator():
    question_list = list(developer_qna.keys())
    win_score = 0
    lose_score = 0
    random_question_length = 5

    selected_question = random.sample(question_list, random_question_length)
    for question in selected_question:
        print(question)
        user_answer = input("Enter your answer: ").lower().strip()
        correct_answer = developer_qna[question]
        if user_answer == correct_answer.lower():
            win_score += 1
            print("Correct!")
        else:
            lose_score += 1
            print("Incorrect!")
    print("You got " + str(win_score) + "/" + str(lose_score) + ".")

project_score_calculator()


