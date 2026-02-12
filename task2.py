def letter_to_num_mapping():
    """Creates a mapping from letters (A-Z) to numbers (0-25)."""
    letter_to_num = {chr(i+65): i for i in range(26)}  # A=0, ..., Z=25
    num_to_letter = {i: chr(i+65) for i in range(26)}  # 0=A, ..., 25=Z
    return letter_to_num, num_to_letter

def decrypt(ciphertext, key):
    """Decrypts the given ciphertext using the key with modular subtraction."""
    # Get mappings
    letter_to_num, num_to_letter = letter_to_num_mapping()

    # Convert ciphertext and key to numerical values
    cipher_numbers = [letter_to_num[char] for char in ciphertext]
    key_numbers = [letter_to_num[char] for char in key]

    # Decrypt the ciphertext using modular subtraction
    plaintext_numbers = [(cipher_numbers[i] - key_numbers[i]) % 26 for i in range(len(ciphertext))]

    # Convert the resulting numbers back to letters
    plaintext = ''.join([num_to_letter[num] for num in plaintext_numbers])

    # Log intermediate steps for educational purposes
    print("Ciphertext Numbers: ", cipher_numbers)
    print("Key Numbers: ", key_numbers)
    print("Plaintext Numbers: ", plaintext_numbers)

    return plaintext

def main():
    """Main function to decrypt the ciphertext."""
    print("Welcome to the Decryption Program!")

    # Inputs
    ciphertext = input("Enter the ciphertext (only uppercase letters A-Z): ").upper().strip()
    key = input("Enter the key (only uppercase letters A-Z): ").upper().strip()

    # Truncate the key to match the length of the ciphertext
    key = key[:len(ciphertext)]

    # Print inputs
    print("\nInputs:")
    print("Ciphertext: ", ciphertext)
    print("Key (adjusted length): ", key)

    # Perform decryption
    plaintext = decrypt(ciphertext, key)

    # Print the result
    print("\nDecrypted Plaintext: ", plaintext)

if __name__ == "__main__":
    main()
