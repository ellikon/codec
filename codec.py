# Rob's codec file


def encode():
    password = input("Please enter your password to encode: ")
    encoded_password = ""

    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)

    print("Your password has been encoded and stored!")
    return encoded_password


def decode(encoded_password):
    print("To be done by Jake")


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit", end="\n\n")

        option = int(input("Please enter an option: "))
        encoded_password = ""

        match option:
            case 1:
                encoded_password = encode()
            case 2:
                decode(encoded_password)
            case 3:
                exit()


if __name__ == "__main__":
    main()
