import os
import json

def load_passwords():
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        passwords = {}
    return passwords

def save_passwords(passwords):
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def add_password(passwords, website, username, password):
    passwords[website] = {"username": username, "password": password}

def get_password(passwords, website):
    return passwords.get(website)

def delete_password(passwords, website):
    if website in passwords:
        del passwords[website]

def display_passwords(passwords):
    if not passwords:
        print("No passwords stored.")
    else:
        print("Stored Passwords:")
        for website, credentials in passwords.items():
            print(f"Website: {website}")
            print(f"Username: {credentials['username']}")
            print(f"Password: {credentials['password']}")
            print("-" * 20)

def main():
    passwords = load_passwords()

    while True:
        print("\n===== Password Manager =====")
        print("Commands:")
        print("add - Add Password")
        print("get - Get Password")
        print("delete - Delete Password")
        print("display - Display Passwords")
        print("exit - Exit Password Manager")

        command = input("Enter command: ")

        if command == "add":
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(passwords, website, username, password)
            save_passwords(passwords)  # Save passwords after each addition
        elif command == "get":
            website = input("Enter website: ")
            credentials = get_password(passwords, website)
            if credentials:
                print(f"Username: {credentials['username']}")
                print(f"Password: {credentials['password']}")
            else:
                print(f"No password found for {website}.")
        elif command == "delete":
            website = input("Enter website: ")
            delete_password(passwords, website)
            save_passwords(passwords)
        elif command == "display":
            display_passwords(passwords)
        elif command == "exit":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

