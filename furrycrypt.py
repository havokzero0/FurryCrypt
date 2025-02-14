import os
import base64
import random

def owo_encode(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    owo_binary = binary.replace('0', 'UwU').replace('1', 'OwO')
    return owo_binary

def owo_decode(text):
    binary = text.replace('UwU', '0').replace('OwO', '1')
    decoded_text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return decoded_text

def furryfy_filename(filename):
    furry_names = ["Yiffed_Secrets", "PawsOnly", "Fursona_Manifest", "UwU_Data"]
    name, ext = os.path.splitext(filename)
    return random.choice(furry_names) + ext

def encrypt_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
        encrypted = owo_encode(data)
        new_name = furryfy_filename(filename) + ".furcrypt"
        with open(new_name, 'w', encoding='utf-8') as f:
            f.write(encrypted)
        print(f"Your file has been FurryCrypted! New name: {new_name}")
    except FileNotFoundError:
        print("Error: File not found!")

def decrypt_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
        decrypted = owo_decode(data)
        original_name = filename.replace(".furcrypt", "_decrypted.txt")
        with open(original_name, 'w', encoding='utf-8') as f:
            f.write(decrypted)
        print(f"Your file has been un-furryfied! Restored as: {original_name}")
    except FileNotFoundError:
        print("Error: File not found!")

if __name__ == "__main__":
    action = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").strip().lower()
    filename = input("Enter the filename (must be in the same folder): ").strip()
    
    if action == "e":
        encrypt_file(filename)
    elif action == "d":
        decrypt_file(filename)
    else:
        print("Invalid choice! Use 'E' for encryption or 'D' for decryption.")
