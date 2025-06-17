import random
import string

def generate_password(length=12):
    """
    Generates a random password containing uppercase, lowercase,
    digits, and special characters.
    """
    if length < 6:
        raise ValueError("Password should be at least 6 characters long.")

    # 🔐 Define characters to use in password
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # ✅ Use random.choices to pick characters
    password = ''.join(random.choices(all_chars, k=length))

    return password

def main():
    print("🔒 Random Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\n✅ Your secure password:\n{password}\n")
    except ValueError:
        print("❌ Please enter a valid number (minimum 6).")

if __name__ == "__main__":
    main()
