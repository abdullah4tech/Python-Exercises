# Function to register a new user
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Save the user data in a file (e.g., "users.txt")
    with open("users.txt", "a") as outfile:
        outfile.write(f"{username} {password}\n")
    print("Registration successful!")

# Function to check if user credentials are valid
def check_credentials(username, password):
    with open("users.txt", "r") as infile:
        for line in infile:
            user, passw = line.strip().split()
            if user == username and passw == password:
                return True
    return False

# Function to delete a user account
def delete_account(username):
    with open("users.txt", "r") as infile, open("temp.txt", "w") as tempfile:
        for line in infile:
            user, passw = line.strip().split()
            if user != username:
                tempfile.write(f"{user} {passw}\n")
    import os
    os.remove("users.txt")
    os.rename("temp.txt", "users.txt")
    print("Account deleted successfully!")

while True:
    print("1. Register\n2. Login\n3. Delete Account\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        register_user()
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if check_credentials(username, password):
            print("Login successful!")
        else:
            print("Invalid username or password.")
    elif choice == 3:
        username = input("Enter username to delete account: ")
        delete_account(username)
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

    print()
