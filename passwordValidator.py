# Import the required modules
# 're' module provides support for regular expressions in Python
# 'os' module provides a way of using operating system dependent functionality
import re
import os

# This print statement displays a banner with the password requirements.
# The banner is displayed using a multi-line string (denoted by triple quotes).
# The 'r' before the string starts makes this a raw string, which ignores escape characters.
print(r"""
  ____                                     _    _                _
 |  _ \ __ _ ___ _____      _____  _ __ __| |  / \   _ __   __ _| | __ _ _______ _ __
 | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | / _ \ | '_ \ / _` | |/ _` |_  / _ \ '__|
 |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |/ ___ \| | | | (_| | | (_| |/ /  __/ |
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_/_/   \_\_| |_|\__,_|_|\__, /___\___|_|
                                                                   |___/


  Password must:
  - Be at least 8 characters long
  - Contain at least one uppercase letter
  - Contain at least one lowercase letter
  - Contain at least one digit
  - Contain at least one special character
  - Not contain spaces
  - Not contain the word 'password'
""")

# Function to check if the password meets the requirements
def password_checker(password):
    # Initialize an empty list to hold error messages
    errors = []

    # Check the password against various criteria
    # The password must be at least 8 characters long
    if len(password) < 8:
        errors.append("be at least 8 characters long")

    # The password must contain at least one uppercase letter
    if not re.search("[A-Z]", password):
        errors.append("contain at least one uppercase letter")

    # The password must contain at least one lowercase letter
    if not re.search("[a-z]", password):
        errors.append("contain at least one lowercase letter")

    # The password must contain at least one digit
    if not re.search("[0-9]", password):
        errors.append("contain at least one digit")

    # The password must contain at least one special character
    if not re.search("[^A-Za-z0-9]", password):
        errors.append("contain at least one special character")

    # The password must not contain spaces
    if " " in password:
        errors.append("not contain spaces")

    # The password must not contain the word 'password'
    if "password" in password.lower():
        errors.append("not contain the word 'password'")

    # Return the list of errors. If there are no errors, an empty list is returned
    return errors

# This is the main function that prompts the user for a password and checks it.
# If the password is valid, it asks the user if they want to save it to a file.
def main():
    # Keep asking for a password until a valid one is entered
    while True:
        password = input("Enter your password: ")

        # Check if the password is not empty
        if password:
            # Check the password for errors
            errors = password_checker(password)

            # If there are errors, print them
            if errors:
                print("Your password failed to meet the requirements.")
                error_message = "Please correct the following errors in your password: " + ', '.join(["it should " + error for error in errors]) + "."
                print(error_message)
            else:
                # If there are no errors, the password is valid
                print("Password is valid.")
                # Ask the user if they want to save the password to a file
                while True:
                    choice = input("Do you want to save the password to a file? (yes/no): ")

                    # If they choose to save it
                    if choice.lower() in ['yes', 'y']:
                        # Set the output path
                        output_path = 'password.txt'

                        # Write the password to the file
                        with open(output_path, 'w') as f:
                            f.write(password)

                        # Print the absolute path of the file where the password was saved
                        print(f"Password saved to: {os.path.abspath(output_path)}")

                        # Wait for the user to press a key before closing the console
                        input("Press any key to exit...")
                        break

                    # If they choose not to save it
                    elif choice.lower() in ['no', 'n']:
                        # Print the password to the console
                        print("You can copy password from here: " + password)

                        # Wait for the user to press a key before closing the console
                        input("Press any key to exit...")
                        break

                    # If they enter something other than 'yes' or 'no'
                    else:
                        print("Invalid choice. Please enter 'yes' or 'no'.")
                break

        # If the password is empty
        else:
            print("Password cannot be empty. Please enter a password.")

# Call the main function
if __name__ == "__main__":
    main()
