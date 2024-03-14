username = 'Aneesa'

password = 'Aneesa_00'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("You have logged into the system.")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")