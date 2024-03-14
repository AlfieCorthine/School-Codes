import sys
import time
import string

def check(password):
    symbols = "!$%^&*()-_=+"
    score = len(password)

    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    symbol = any(char in symbols for char in password)

    if upper:
        score += 5
    if lower:
        score += 5
    if digit:
        score += 5     
    if symbol:
        score += 5
    if upper and lower and digit and symbol:
        score += 10
    if password.isalpha() and not (upper or lower):
        score -= 5
    if password.isdigit():
        score -= 5
    if all(char in symbols for char in password):
        score -= 5

    return score

def strength(score):
    if score > 20:
        return "Strong"
    elif score >= 6:
        return "Medium"
    else:
        return "Weak"

while True:
    print('''
    - === - Menu - === -
    1. Password Checker 
    2. Quit
    ''')
    menu = int(input("Enter your selection > "))

    if menu == 1:
        password = input("Enter your password > ")

        if len(password) < 8 or len(password) > 24:
            print("Please enter a number between 8 and 24")
            continue
        if any(char not in string.ascii_letters + string.digits + "!$%^&*()-_=+" for char in password):
            print("Password contains invalid characters")
            continue

        score = check(password)
        password_strength = strength(score)
        time.sleep(0.8)
        print(f"Password length {len(password)}")
        time.sleep(0.8)
        print(f"Password score: {score}")
        time.sleep(0.8)
        print(f"Password Strength: {password_strength}")
        time.sleep(0.8)
        sys.exit()

    elif menu == 2:
        sys.stdout.write("Exiting")
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        print()
        sys.exit()

    else:
        print("Invalid number selection")


