# pylint: disable=E0401
import sqlite3
import bcrypt
import random

# Create a connection to the SQLite database
conn = sqlite3.connect("gambling_app.db")
cursor = conn.cursor()

# Drop the existing users table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# Create the user table with the correct schema
cursor.execute(
    """
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        points INTEGER DEFAULT 0
    )
"""
)
conn.commit()


def encrypt_password(password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)
    return password_hash


def register_user(username, password):
    password_hash = encrypt_password(password)
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash),
        )
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose another username.")


logged_in_user = None  # Global variable to store the logged-in user


def login_user(username, password):
    global logged_in_user  # Access the global variable
    cursor.execute("SELECT password_hash FROM users WHERE username=?", (username,))
    row = cursor.fetchone()
    if row and bcrypt.checkpw(password.encode("utf-8"), row[0]):
        print("Login successful!")
        logged_in_user = username  # Update the logged_in_user variable
    else:
        print("Invalid username or password.")


def generate_random_number():
    return random.randint(1, 10)


def play_game():
    if not logged_in_user:
        print("Please log in first.")
        return

    print("Welcome to the Number Generator Game!")
    print("Guess a number between 1 and 10.")
    target_number = generate_random_number()

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess == target_number:
                print("Congratulations! You guessed the correct number.")
                # Update user points in the database
                cursor.execute(
                    "UPDATE users SET points = points + 1 WHERE username=?",
                    (logged_in_user,),
                )
                conn.commit()
                break
            else:
                print("Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def view_wallet():
    if not logged_in_user:
        print("Please log in first.")
        return

    # Retrieve user points from the database
    cursor.execute("SELECT points FROM users WHERE username=?", (logged_in_user,))
    row = cursor.fetchone()
    if row:
        points = row[0]
        print(f"Wallet: {points} gold coins")
    else:
        print("Error: Unable to fetch wallet information.")


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Play")
        print("4. View Wallet")  # New menu option
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login_user(username, password)
        elif choice == "3":
            play_game()
        elif choice == "4":
            view_wallet()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
