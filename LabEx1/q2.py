def authenticate():
    username = input("Enter your username (alphabetical characters only): ").strip()

    if not username.isalpha():
        print("Error: Username must contain only alphabetical characters.")
        return False

    password = input("Enter your password (at least 5 numeric characters): ").strip()

    if not password.isdigit():
        print("Your password must contain only numeric characters.")
        return False
    elif len(password) < 5:
        print("Your password need to contain at least 5 characters.")
        return False

    # If both username and password are valid
    print("Authentication successful!")
    return True

# Call the authenticate function
authenticate()
