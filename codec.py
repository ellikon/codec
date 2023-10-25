# Rob's codec file
password = ""
encoded_password = ""

def encode():
    global password
    global encoded_password
    password = input("Please enter your password to encode: ")
    encoded_password = ""

    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)

    print("Your password has been encoded and stored!")
    return encoded_password


def decode(encoded_password):
    print(f"The encoded password is {encoded_password}, and the original password is {password}.")


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit", end="\n\n")

        option = int(input("Please enter an option: "))

        match option:
            case 1:
                encoded_password = encode()
            case 2:
                decode(encoded_password)
            case 3:
                exit()


if __name__ == "__main__":
    main()
