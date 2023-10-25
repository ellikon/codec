# Rob's codec file

def encode():
    password = input("Data to encode: ")
    encoded_password = ""

    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)

    print(f"Encoded data: {encoded_password}")


def main():
    while True:
        print("0. Exit")
        print("1. Encode")
        print("2. Decode", end="\n\n")

        option = int(input("Menu option: "))

        match option:
            case 0:
                exit()
            case 1:
                encode()


if __name__ == "__main__":
    main()
