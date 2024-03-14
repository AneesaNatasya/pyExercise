def login():
    password = "password123"
    attempts = 5

    while attempts > 0:
        user_input = input("Enter the password: ")

        if user_input == password:
            print("Logged in to the system.")
            return

        attempts -= 1
        if attempts > 0:
            print("Incorrect password. Please try again.")
            print(f"{attempts} attempts remaining.")
        else:
            print("You have been blocked from the system after five unsuccessful tries.")

if __name__ == "__main__":
    login()
