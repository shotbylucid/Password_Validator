import re
import os

print(r"""
Password requirements:
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
	if len(password) < 8:
		errors.append("be at least 8 characters long")
	if not re.search("[A-Z]", password):
		errors.append("contain at least one uppercase letter")
	if not re.search("[a-z]", password):
		errors.append("contain at least one lowercase letter")
	if not re.search("[0-9]", password):
		errors.append("contain at least one digit")
	if not re.search("[^A-Za-z0-9]", password):
		errors.append("contain at least one special character")
	if " " in password:
		errors.append("not contain spaces")
	if "password" in password.lower():
		errors.append("not contain the word 'password'")

	# If there are any errors, return them
	if errors:
		return errors
	else:
		return []

def main():
    while True:
        password = input("Enter your password: ")
        print(f"Password entered: {password}")  # Debug print
        if password: # Check if the password is not empty
            errors = password_checker(password)
            if errors:
                print("Your password failed to meet the requirements.")
                print("Please correct the following errors in your password: " + 'and '.join([error for error in errors]))
            else:
                print("Password is compliant.")
                break
        else:
            print("Password cannot be empty. Please enter a password.")

main()