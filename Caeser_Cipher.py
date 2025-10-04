def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "e":  # encrypt
                result += chr((ord(char) - base + shift) % 26 + base)
            else:  # decrypt
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


def main():
    print("=== Caesar Cipher Program ===")
    while True:
        mode = input("\nEnter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if mode == 'q':
            print("Exiting program. Goodbye!")
            break
        if mode not in ('e', 'd'):
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")
            continue

        message = input("Enter your message: ")
        
        while True:
            shift_input = input("Enter shift value (number): ")
            if shift_input.isdigit():
                shift = int(shift_input)
                break
            else:
                print("Please enter a valid number.")

        output = caesar_cipher(message, shift, mode)
        print(f"\nResult: {output}")

    input("\nPress Enter to close the program...")


if __name__ == "__main__":
    main()
