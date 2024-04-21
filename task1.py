def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted = (ord(char) - 97 + shift if mode == 'encrypt' else ord(char) - 97 - shift) % 26 + 97
            else:
                shifted = (ord(char) - 65 + shift if mode == 'encrypt' else ord(char) - 65 - shift) % 26 + 65
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (encrypt/decrypt/exit): ").lower()
        if choice == 'exit':
            break
        elif choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please choose 'encrypt', 'decrypt', or 'exit'.")
            continue
        
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value (an integer): "))
        
        if choice == 'encrypt':
            encrypted_text = caesar_cipher(text, shift, 'encrypt')
            print("Encrypted message:", encrypted_text)
        elif choice == 'decrypt':
            decrypted_text = caesar_cipher(text, shift, 'decrypt')
            print("Decrypted message:", decrypted_text)

if __name__ == "__main__":
    main()
