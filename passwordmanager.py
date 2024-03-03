import sqlite3
import hashlib
from cryptography.fernet import Fernet  # for AES encryption
import base64
import random
import string

# Function to generate a strong password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
# Generate a Fernet key
def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_password(password, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password)
    return decrypted_password.decode()

# Example usage
def main():
    key = generate_fernet_key()

    while True:
        print("\n1. Add Password")
        print("2. Retrieve Password")
        print("3. Generate Strong Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password: ")
            encrypted_password = encrypt_password(password, key)
            print(f"Password for {account} encrypted successfully.")
        elif choice == "2":
            account = input("Enter account name: ")
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"Retrieved decrypted password for {account}: {decrypted_password}")
        elif choice == '3':
            length = int(input("Enter password length: "))
            print("Generated Password:", generate_password(length))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
