import re

def check_password_strength(password):
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = bool(re.match('[$&+,:;=?@#|\'<>.^*()%!-]', password))

    strength = 0
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Moderate"
    else:
        return "Strong"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
