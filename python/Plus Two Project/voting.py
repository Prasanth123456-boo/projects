import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="voting_system"
)

cursor = db.cursor()

def register_voter():
    username = input("Enter a unique username: ")
    password = input("Enter a password: ")

    cursor.execute("SELECT * FROM voters WHERE username = %s", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose another.")
    else:
        cursor.execute("INSERT INTO voters (username, password, is_voted) VALUES (%s, %s, 0)", (username, password))
        db.commit()
        print("Voter registered successfully!")

def register_candidate():
    name = input("Enter candidate's name: ")
    party = input("Enter candidate's party: ")

    cursor.execute("INSERT INTO candidates (name, party) VALUES (%s, %s)", (name, party))
    db.commit()
    print("Candidate registered successfully!")

def vote():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM voters WHERE username = %s AND password = %s AND is_voted = 0", (username, password))
    voter = cursor.fetchone()

    if voter:
        print("Candidates:")
        cursor.execute("SELECT * FROM candidates")
        candidates = cursor.fetchall()

        for candidate in candidates:
            print(f"{candidate[0]}. {candidate[1]} ({candidate[2]})")

        candidate_id = int(input("Enter the candidate's ID you want to vote for: "))

        cursor.execute("INSERT INTO votes (voter_id, candidate_id) VALUES (%s, %s)", (voter[0], candidate_id))
        cursor.execute("UPDATE voters SET is_voted = 1 WHERE voter_id = %s", (voter[0],))
        db.commit()
        print("Vote cast successfully!")

    else:
        print("Invalid credentials or you have already voted.")

def main():
    while True:
        print("\nVoting System")
        print("1. Register Voter")
        print("2. Register Candidate")
        print("3. Vote")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_voter()
        elif choice == '2':
            register_candidate()
        elif choice == '3':
            vote()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    db.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()

# CREATE DATABASE voting_system;

# CREATE TABLE voters (
#     voter_id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(255) NOT NULL UNIQUE,
#     password VARCHAR(255) NOT NULL,
#     is_voted BOOLEAN DEFAULT FALSE
# );

# CREATE TABLE candidates (
#     candidate_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     party VARCHAR(255) NOT NULL
# );

# CREATE TABLE votes (
#     vote_id INT AUTO_INCREMENT PRIMARY KEY,
#     voter_id INT,
#     candidate_id INT,
#     vote_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (voter_id) REFERENCES voters(voter_id),
#     FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
# );
