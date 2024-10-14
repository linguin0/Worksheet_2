User_Password = input("Enter password > ")

def CharacterCheck(Password):
    if not Password.isalpha() and not Password.isnumeric():
        return True
    return False

if len(User_Password) >= 8 and CharacterCheck(User_Password):
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")