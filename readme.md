# Password Strength Checker

This is a Python-based password strength checker that evaluates the strength of a given password based on various criteria. It checks for the presence of uppercase and lowercase letters, digits, special characters, common password patterns, repeated characters, and length. The program reads a list of common passwords from a file and checks if the entered password is common.

## Features
- **Length Check**: Password must be at least 9 characters long.
- **Uppercase Letters**: Password should contain at least one uppercase letter.
- **Lowercase Letters**: Password should contain at least one lowercase letter.
- **Digits**: Password should contain at least one numeric digit.
- **Special Characters**: Password should contain at least one special character (e.g., `!@#$%^&*`).
- **Common Password Check**: Compares the password against a list of common passwords and flags it if it's a common one.
- **Repeated Characters**: Password is flagged if it contains more than 2 consecutive repeated characters.
- **Strength Evaluation**: Provides a detailed feedback on password strength.

## Installation

1. Clone the repository or download the files.
2. Create a file named `common_passwords.txt` in the same directory as the Python script. This file should contain a list of common passwords, one per line.
   
   Example content for `common_passwords.txt`:

3. Ensure you have Python 3 installed on your system.

4. Run the Python script `password_strength_checker.py`.

```bash
python password_strength_checker.py

