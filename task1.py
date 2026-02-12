def letter_to_num_mapping():
    """Creates a mapping from letters (A-Z) to numbers (0-25)."""
    letter_to_num = {chr(i+65): i for i in range(26)}  # A=0, B=1, ..., Z=25
    num_to_letter = {i: chr(i+65) for i in range(26)}  # 0=A, 1=B, ..., 25=Z
    return letter_to_num, num_to_letter

def validate_input(plaintext, key):
    """Validates the input to ensure all characters are uppercase A-Z and non-empty."""
    if not plaintext.isalpha() or not key.isalpha():
        raise ValueError("Both plaintext and key must contain only uppercase letters (A-Z).")
    
    if len(plaintext) == 0 or len(key) == 0:
        raise ValueError("Neither the plaintext nor the key can be empty.")
    
    if len(plaintext) > len(key):
        raise ValueError("The length of the key must be at least as long as the plaintext.")
    
    return True

def encrypt(plaintext, key):
    """Encrypts the given plaintext using the key with modular addition."""
    # Get the mappings from letter to number and number to letter
    letter_to_num, num_to_letter = letter_to_num_mapping()

    # Convert plaintext and key to their numerical representations
    plaintext_numbers = [letter_to_num[char] for char in plaintext]  # Convert each letter to a number
    key_numbers = [letter_to_num[char] for char in key]  # Convert key to a list of numbers

    # Encrypt the message using modular addition
    cipher_numbers = [(plaintext_numbers[i] + key_numbers[i]) % 26 for i in range(len(plaintext))]

    # Convert cipher numbers back to letters using num_to_letter mapping
    cipher = ''.join([num_to_letter[num] for num in cipher_numbers])

    # Log intermediate steps for educational purposes
    print("Plaintext Numbers: ", plaintext_numbers)
    print("Key Numbers: ", key_numbers)
    print("Cipher Numbers: ", cipher_numbers)

    return cipher

def get_input():
    """Gets input from the user for plaintext and key."""
    # Get plaintext input from the user
    plaintext = input("Enter the plaintext (only uppercase letters A-Z): ").upper().strip()

    # Get key input from the user
    key = input("Enter the key (only uppercase letters A-Z): ").upper().strip()

    return plaintext, key

def main():
    """Main function to run the encryption process."""
    print("Welcome to the Symmetric Encryption Program!")
    
    try:
        # Get input from the user
        plaintext, key = get_input()

        # Validate the input
        validate_input(plaintext, key)
        
        # Truncate or expand the key to match the length of the plaintext
        key = key[:len(plaintext)]  # Truncate key if it's longer than plaintext
        
        print("\nInitial Inputs:")
        print("Plaintext: ", plaintext)
        print("Key (adjusted length): ", key)

        # Perform encryption
        cipher = encrypt(plaintext, key)

        # Output the final result
        print("\nEncrypted message (Ciphertext):", cipher)

        # Provide more information about the encryption process
        print("\nEncryption Steps:")
        print(f"1. Convert each letter in the plaintext to its numerical equivalent (0-25).")
        print(f"2. Convert each letter in the key to its numerical equivalent (0-25).")
        print(f"3. Apply modular addition: (plaintext_number + key_number) % 26.")
        print(f"4. Convert the resulting numbers back to letters to form the ciphertext.")
    
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
