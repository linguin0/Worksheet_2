try:
    Grade = int(input("Enter your numerical grade > "))
    match Grade:
        case Grade if Grade >= 80:
            print("You got an A!")
        case Grade if Grade <= 79 and Grade >= 60:
            print("You got a B!")
        case Grade if Grade <= 59 and Grade >= 50:
            print("You got a C!")
        case Grade if Grade <= 49 and Grade >= 40:
            print("You got a D!")
        case Grade if Grade <= 39 and Grade >= 0:
            print("You got an F")
        case _:
            print("Error: Grades must be between 0 and 100")
except:
    print("Error: Please enter a number")