try:
    Grade = int(input("Enter your numerical grade > "))
    if Grade < 0 or Grade > 100:
        print("Error: Grades must be between 0 and 100")
    else:
        match Grade:
            case Grade if Grade >= 80:
                print("Your grade is: A")
            case Grade if Grade <= 79 and Grade >= 60:
                print("Your grade is: B")
            case Grade if Grade <= 59 and Grade >= 50:
                print("Your grade is: C")
            case Grade if Grade <= 49 and Grade >= 40:
                print("Your grade is: D")
            case Grade if Grade <= 39 and Grade >= 0:
                print("Your grade is: F")
except:
    print("Error: Please enter a number")