def calc():
    a = int(input("Enter the first number"))
    b = int(input("Enter the Second number"))


    print("Press 1 For Addition")
    print("Press 2 for substraction")
    print("Press 3 Multiplication")
    print("Press 4 for Division")

    choice1 = int(input("Enter Choice"))

    if choice1 == 1:
        print("You Chose Addition")
        print(a+b)
    elif choice1 == 2:
        print("You choose substraction")
        print(a-b)

    elif choice1 == 3:
        print("You choose multiplication")
        print(a*b)
    elif choice1 == 4:
        print("You choose Division")
        print(a/b)
calc()