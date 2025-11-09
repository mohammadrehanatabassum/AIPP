import os
import json
from hashlib import pbkdf2_hmac

USERS_FILE = "users.json"
ITERATIONS = 200_000

# ---------------- Helper Functions ---------------- #

def _load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

def hash_password(password: str):
    salt = os.urandom(16)
    dk = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
    return salt.hex(), dk.hex()

def verify_password(password: str, salt_hex: str, hash_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    expected = bytes.fromhex(hash_hex)
    dk = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
    return dk == expected

# ---------------- Register Function ---------------- #

def register(username: str):
    users = _load_users()
    if username in users:
        print("⚠️  Username already exists.")
        return

    password = input("Choose password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("❌ Passwords do not match.")
        return

    salt, hash_hex = hash_password(password)
    users[username] = {"salt": salt, "hash": hash_hex}
    _save_users(users)
    print(f"✅ User '{username}' registered successfully!")

# ---------------- Login Function ---------------- #

def login(username: str):
    users = _load_users()
    if username not in users:
        print("❌ User not found.")
        return

    password = input("Enter password: ")
    data = users[username]
    if verify_password(password, data["salt"], data["hash"]):
        print(f"✅ Login successful! Welcome, {username}.")
    else:
        print("❌ Invalid password.")

# ---------------- Main Menu ---------------- #

def main():
    print("=== Simple Demo Login System ===")
    while True:
        print("\n1) Register  2) Login  3) Quit")
        choice = input("> ").strip()
        if choice == "1":
            username = input("Choose username: ")
            register(username)
        elif choice == "2":
            username = input("Enter username: ")
            login(username)
        elif choice == "3" or choice.lower() in ("q", "quit"):
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Please choose 1, 2 or 3.")

# ---------------- Run the Program ---------------- #

if __name__ == "__main__":
    main()
