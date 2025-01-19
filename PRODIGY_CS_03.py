import re

# Load common passwords from the file
with open('common_passwords.txt', 'r') as file:
    common_passwords = set(file.read().splitlines())

password = input("Enter your password: ")

# Criteria
min_length = 9
has_uppercase = bool(re.search(r'[A-Z]', password))
has_lowercase = bool(re.search(r'[a-z]', password))
has_digit = bool(re.search(r'\d', password))
has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
has_no_common_patterns = password not in common_passwords
has_repeated_chars = bool(re.search(r'(.)\1{2,}', password))  # Checks for more than 2 consecutive repeated characters
is_length_valid = min_length <= len(password)

# Strength Evaluation
if not is_length_valid:
    print(f"Password must be atleast {min_length}")
else:
    strength = 0
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1
    if has_no_common_patterns:
        strength += 1
    if not has_repeated_chars:
        strength += 1

    # Detailed Feedback
    print(f"Password Length: {'Valid' if is_length_valid else 'Invalid'} (atleast {min_length} characters long)")
    print(f"Contains Uppercase Letters: {'Yes' if has_uppercase else 'No'}")
    print(f"Contains Lowercase Letters: {'Yes' if has_lowercase else 'No'}")
    print(f"Contains Digits: {'Yes' if has_digit else 'No'}")
    print(f"Contains Special Characters: {'Yes' if has_special_char else 'No'}")
    print(f"Contains Common Patterns: {'No' if has_no_common_patterns else 'Yes'} (This password is common.)")
    print(f"Contains Repeated Characters: {'No' if not has_repeated_chars else 'Yes'}")

    # Final Strength Evaluation
    if strength == 7:
        print("Password is Very Strong.")
    elif strength == 6:
        print("Password is Strong.")
    elif strength == 5:
        print("Password is Medium.")
    elif strength == 4:
        print("Password is Weak.")
    else:
        print("Password is Very Weak. Consider improving length, complexity, and avoiding common patterns.")
