import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_repo"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def add_student(conn, name, roll_number, class_name):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO students (name, roll_number, class) VALUES (%s, %s, %s)"
        values = (name, roll_number, class_name)
        cursor.execute(sql, values)
        conn.commit()
        print("Student added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_course(conn, course_name):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO courses (course_name) VALUES (%s)"
        values = (course_name,)
        cursor.execute(sql, values)
        conn.commit()
        print("Course added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def add_grade(conn, student_id, course_id, grade):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)"
        values = (student_id, course_id, grade)
        cursor.execute(sql, values)
        conn.commit()
        print("Grade added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def generate_report_card(conn, student_id):
    try:
        cursor = conn.cursor()
        sql = """
            SELECT s.name, s.roll_number, s.class, c.course_name, g.grade
            FROM students s
            JOIN grades g ON s.student_id = g.student_id
            JOIN courses c ON g.course_id = c.course_id
            WHERE s.student_id = %s
        """
        cursor.execute(sql, (student_id,))
        report_card = cursor.fetchall()
        if report_card:
            print("Student Report Card:")
            print(f"Student ID: {student_id}")
            for row in report_card:
                print(f"Name: {row[0]}, Roll Number: {row[1]}, Class: {row[2]}, Course: {row[3]}, Grade: {row[4]}")
        else:
            print("No grades found for this student.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

while True:
    print("\nStudent Report Card System")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Grade")
    print("4. Generate Report Card")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter student roll number: ")
        class_name = input("Enter student class: ")
        conn = connect_to_database()
        if conn:
            add_student(conn, name, roll_number, class_name)
            conn.close()
    elif choice == '2':
        course_name = input("Enter course name: ")
        conn = connect_to_database()
        if conn:
            add_course(conn, course_name)
            conn.close()
    elif choice == '3':
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        grade = input("Enter grade: ")
        conn = connect_to_database()
        if conn:
            add_grade(conn, student_id, course_id, grade)
            conn.close()
    elif choice == '4':
        student_id = int(input("Enter student ID to generate report card: "))
        conn = connect_to_database()
        if conn:
            generate_report_card(conn, student_id)
            conn.close()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


# This code is used to create table
#  CREATE TABLE students (
#     student_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     roll_number VARCHAR(20) NOT NULL,
#     class VARCHAR(20) NOT NULL
# );

# CREATE TABLE courses (
#     course_id INT AUTO_INCREMENT PRIMARY KEY,
#     course_name VARCHAR(255) NOT NULL
# );

# CREATE TABLE grades (
#     grade_id INT AUTO_INCREMENT PRIMARY KEY,
#     student_id INT,
#     course_id INT,
#     grade VARCHAR(2),
#     FOREIGN KEY (student_id) REFERENCES students(student_id),
#     FOREIGN KEY (course_id) REFERENCES courses(course_id)
# );