import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        grade FLOAT
    )
''')

def add_student(name, age, grade):
    sql = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(sql, values)
    conn.commit()
    print("Student added successfully!")

def display_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    
    if not students:
        print("No students found.")
    else:
        print("ID | Name | Age | Grade")
        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))
        add_student(name, age, grade)
    elif choice == '2':
        display_students()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
