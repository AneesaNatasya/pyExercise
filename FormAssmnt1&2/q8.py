def login_system(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username not in users:
        print("Invalid username. You are not a valid user of the system.")
    elif users[username] != password:
        print("Invalid password. Please try again.")
    else:
        print("Logged in to the system.")

def main():
    # Dictionary containing usernames and passwords
    users = {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5",
        "user6": "password6",
        "user7": "password7",
        "user8": "password8",
        "user9": "password9",
        "user10": "password10"
    }

    # Call the login_system function with the users dictionary
    login_system(users)

if __name__ == "__main__":
    main()

