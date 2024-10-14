Day = input("Enter a day of the week > ").lower()
DaysOfWeek = [("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7)]

Found = False

for Item in DaysOfWeek:
    if Item[0] == Day:
        print(f"{Day.capitalize()} is day {Item[1]}")
        Found = True
if not Found:
    print("Please enter a valid day")