import re
from getpass import getpass  # hides what you type

SPECIALS = r"!@#$%^&*()\-_=+\[\]{};:'\",.<>/?`~\\|"

def password_strength(password: str):
    # Length & character-class checks
    length_ok       = len(password) >= 8
    has_upper       = re.search(r"[A-Z]", password) is not None
    has_lower       = re.search(r"[a-z]", password) is not None
    has_digit       = re.search(r"[0-9]", password) is not None
    has_special     = re.search(f"[{re.escape(SPECIALS)}]", password) is not None

    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        rating = "Very Strong"
    elif score == 4:
        rating = "Strong"
    elif score == 3:
        rating = "Moderate"
    elif score == 2:
        rating = "Weak"
    else:
        rating = "Very Weak"

    details = {
        "Length ≥ 8": length_ok,
        "Uppercase": has_upper,
        "Lowercase": has_lower,
        "Digit": has_digit,
        "Special": has_special,
    }
    return rating, details

if __name__ == "__main__":
    pwd = getpass("Enter your password (hidden): ")
    rating, details = password_strength(pwd)

    print(f"\nPassword Strength: {rating}")
    for k, v in details.items():
        print(f"- {k}: {'✔️' if v else '❌'}")