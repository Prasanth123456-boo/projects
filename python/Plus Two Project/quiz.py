import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="quiz_app"
)

cursor = db.cursor()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Quiz:
    def __init__(self, title, author_username):
        self.title = title
        self.author_username = author_username

class Question:
    def __init__(self, question_text, quiz_id):
        self.question_text = question_text
        self.quiz_id = quiz_id

class Answer:
    def __init__(self, answer_text, question_id, is_correct):
        self.answer_text = answer_text
        self.question_id = question_id
        self.is_correct = is_correct

def register_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()
    print("User registered successfully!")

def create_quiz(title, author_username):
    cursor.execute("INSERT INTO quizzes (title, author_username) VALUES (%s, %s)", (title, author_username))
    db.commit()
    print("Quiz created successfully!")

def add_question(question_text, quiz_id):
    cursor.execute("INSERT INTO questions (question_text, quiz_id) VALUES (%s, %s)", (question_text, quiz_id))
    db.commit()
    print("Question added successfully!")

def add_answer(answer_text, question_id, is_correct):
    cursor.execute("INSERT INTO answers (answer_text, question_id, is_correct) VALUES (%s, %s, %s)",
                   (answer_text, question_id, is_correct))
    db.commit()
    print("Answer added successfully!")

def start_quiz(quiz_id, username):
    cursor.execute("SELECT * FROM quizzes WHERE quiz_id = %s", (quiz_id,))
    quiz = cursor.fetchone()

    if quiz:
        print(f"Starting quiz: {quiz[1]}")

        cursor.execute("SELECT * FROM questions WHERE quiz_id = %s", (quiz_id,))
        questions = cursor.fetchall()

        for question in questions:
            print(question[2])

            cursor.execute("SELECT * FROM answers WHERE question_id = %s", (question[0],))
            answers = cursor.fetchall()

            for answer in answers:
                print(f"{answer[0]}. {answer[2]}")

            user_answer = input("Enter your answer (answer ID): ")

            # Check if the user's answer is correct
            cursor.execute("SELECT is_correct FROM answers WHERE answer_id = %s", (user_answer,))
            is_correct = cursor.fetchone()

            if is_correct and is_correct[0]:
                print("Correct!\n")
            else:
                print("Incorrect!\n")

        print("Quiz completed.")
    else:
        print("Invalid quiz ID.")

def main():
    while True:
        print("\nQuiz App Menu")
        print("1. Register User")
        print("2. Create Quiz")
        print("3. Add Question")
        print("4. Add Answer")
        print("5. Start Quiz")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
        elif choice == '2':
            title = input("Enter quiz title: ")
            author_username = input("Enter your username: ")
            create_quiz(title, author_username)
        elif choice == '3':
            question_text = input("Enter question text: ")
            quiz_id = int(input("Enter quiz ID: "))
            add_question(question_text, quiz_id)
        elif choice == '4':
            answer_text = input("Enter answer text: ")
            question_id = int(input("Enter question ID: "))
            is_correct = input("Is this answer correct? (yes/no): ").lower() == 'yes'
            add_answer(answer_text, question_id, is_correct)
        elif choice == '5':
            quiz_id = int(input("Enter quiz ID: "))
            username = input("Enter your username: ")
            start_quiz(quiz_id, username)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    db.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
