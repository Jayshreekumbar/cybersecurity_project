from cryptography.fernet import Fernet

# Generate Key and save to secret.key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as secret.key")

# Load the key from file
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt File
def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        original_data = file.read()
    encrypted_data = f.encrypt(original_data)
    with open(filename + ".enc", "wb") as enc_file:
        enc_file.write(encrypted_data)
    print(f"File {filename} encrypted as {filename}.enc")

# Decrypt File
def decrypt_file(encrypted_filename, key):
    f = Fernet(key)
    with open(encrypted_filename, "rb") as enc_file:
        encrypted_data = enc_file.read()
    decrypted_data = f.decrypt(encrypted_data)
    # Remove .enc and add _decrypted
    output_file = encrypted_filename.replace(".enc", "_decrypted")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted_data)
    print(f"File {encrypted_filename} decrypted as {output_file}")

# Main Execution
if __name__ == "__main__":
    print("--- Data Security and File Encryption ---")
    print("1. Generate Key (gen)")
    print("2. Encrypt File (enc)")
    print("3. Decrypt File (dec)")
    
    choice = input("Enter choice (gen/enc/dec): ").lower()

    if choice == "gen":
        generate_key()
    elif choice == "enc":
        try:
            key = load_key()
            filename = input("Enter filename to encrypt: ")
            encrypt_file(filename, key)
        except FileNotFoundError:
            print("Error: secret.key not found. Please generate key first (gen).")
    elif choice == "dec":
        try:
            key = load_key()
            enc_filename = input("Enter encrypted filename (.enc): ")
            decrypt_file(enc_filename, key)
        except FileNotFoundError:
            print("Error: Key or encrypted file not found.")
    else:
        print("Invalid choice!")