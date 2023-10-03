import pickle

s = []
found = False
validated=1

try:
    fin = open("stud1.dat", "rb+")
    h = int(input("Enter the roll number to be searched: "))
    
    while True:
        n = fin.tell()
        try:
            s = pickle.load(fin)
        except EOFError:
            break  # Exit the loop when there are no more records to read
            print(s)
        if s[0] == h:
            print(s[1])
            m = input("Enter the new name: ")
            s[1] = m
            fin.seek(n)
            pickle.dump(s, fin)
            found = True
            validated=0
        if validated==0:
            print("Updated successfully")
            break
        else:
            print("No Rerord")
            break

except EOFError:
    if found:
        print("File Found")
    else:
        print("Not found")
    fin.close()
