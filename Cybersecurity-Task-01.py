"""
Password Strength Checker
DecodeLabs Cyber Security - Project 1

Evaluates a password as WEAK, MEDIUM, or STRONG based on:
  - Length
  - Use of uppercase letters
  - Use of numbers
  - Use of special symbols
"""

import string


def check_password_strength(password: str) -> dict:
    """
    Analyze a password and return its strength details.

    Returns a dict with:
        length_ok, has_upper, has_lower, has_digit, has_symbol,
        score, strength
    """
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    # Each satisfied condition adds one point
    score = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

    # Immediate fail: passwords under 8 characters are always weak,
    # regardless of character variety (exponential brute-force risk)
    if not length_ok:
        strength = "WEAK"
    elif score <= 2:
        strength = "WEAK"
    elif score in (3, 4):
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return {
        "length_ok": length_ok,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "score": score,
        "strength": strength,
    }


def print_report(password: str, result: dict) -> None:
    """Pretty-print the strength report for a password."""
    print("\n--- Password Strength Report ---")
    print(f"Password length : {len(password)} chars "
          f"({'OK' if result['length_ok'] else 'too short, need 8+'})")
    print(f"Uppercase letter: {'Yes' if result['has_upper'] else 'No'}")
    print(f"Lowercase letter: {'Yes' if result['has_lower'] else 'No'}")
    print(f"Contains number : {'Yes' if result['has_digit'] else 'No'}")
    print(f"Contains symbol : {'Yes' if result['has_symbol'] else 'No'}")
    print(f"Score           : {result['score']}/5")
    print(f"Strength        : {result['strength']}")
    print("---------------------------------\n")


def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type 'quit' to exit.\n")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "quit":
            print("Goodbye!")
            break
        if password == "":
            print("Please enter a non-empty password.\n")
            continue

        result = check_password_strength(password)
        print_report(password, result)


if __name__ == "__main__":
    main()