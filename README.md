# Password Validator

This Python script checks if a password meets certain requirements. The requirements are:

- The password must be at least 8 characters long
- It must contain at least one uppercase letter
- It must contain at least one lowercase letter
- It must contain at least one digit
- It must contain at least one special character
- It should not contain spaces
- It should not contain the word 'password'

## Usage

To use this script, simply run it in a Python environment. The script will prompt you to enter a password. If the password does not meet the requirements, the script will tell you what requirements were not met. If the password is valid, the script will ask if you want to save the password to a file.

## Dependencies

This script uses the `re` and `os` modules from the Python Standard Library.

## Example

```bash
# Run the script with the follow command in your console of choice

python passwordValidator.py

# Or use the following command if the above for mentioned command doesn't work

python3 passwordValidator.py
```
