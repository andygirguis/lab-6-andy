# andy
def encode(password: str) -> str:
    encoded = []
    for char in password:
        if char.isdigit():
            # Increment the number by 3 and take modulo 10 to wrap around beteen 0-9
            encoded_char = str((int(char) + 3) % 10)
        else:
            encoded_char = char  # If it's not a digit, keep it unchanged
        encoded.append(encoded_char)
    return ''.join(encoded)


def decode(encoded_password: str) -> str:
    decoded = []
    for char in encoded_password:
        if char.isdigit():
            # Decrement the number by 3 and take modulo 10 to wrap around between 0-9
            decoded_char = str((int(char) - 3) % 10)
        else:
            decoded_char = char  # If it's not a digit, keep it unchanged
        decoded.append(decoded_char)
    return ''.join(decoded)


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!\n")


        elif option == "2":

            print(
                f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")

        elif option == "3":

            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()