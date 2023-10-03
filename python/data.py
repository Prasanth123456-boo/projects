import pickle #import pickle to use binary file

def create_student_data(file_name): # create a function to crate a pickle file and insert value to that particular file
    student_data = []

    try:
        fin = open(file_name, "rb+")
        try:
            while True:
                s = pickle.load(fin)
                student_data.append(s)
        except EOFError:
            fin.close()
    except FileNotFoundError:
        # If the file doesn't exist, create it
        fin = open(file_name, "wb")

    while True:
        roll_number = int(input("Enter roll number (0 to stop): "))
        if roll_number == 0:
            break
        name = input("Enter name: ")
        student_data.append([roll_number, name])

    with open(file_name, "wb") as fout:
        for s in student_data:
            pickle.dump(s, fout)

if __name__ == "__main__":
    file_name = "stud1.dat"
    create_student_data(file_name)