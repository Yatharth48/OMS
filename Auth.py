import json
import bcrypt

def load_users():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open('data.json', 'w') as file:
        json.dump(users, file, indent=2)

def register():
    users = load_users()
    username = input("Enter username: ")
    try:
        if username in users:
            print("Username already exists. Try again.")
            return
    except EOFError:
        return{}

    password = input("Enter password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = {'password': hashed_password.decode('utf-8'), 'employees': [], 'departments': []}
    save_users(users)
    print("Registration successful.")

def login(username, password):
    users = load_users()

    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]['password'].encode('utf-8')):
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid credentials. Try again.")
        return False

def logout():
    print("Logging out...")
