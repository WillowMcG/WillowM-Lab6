# Originally made by Willow M

def encode(password):
    encoded = ""
    for char in password:
        char = int(char)
        char = char + 3
        char = str(char)
        encoded += char
    return encoded

def decode(encoded):
    decoded_password = ''
    for i in encoded:
        decoded_password += str(int(i) - 3)
    return decoded_password

def main():

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter the password to encode: ")
            encoded = encode(password)
            print("\nYour password has been encoded and stored!\n")
        elif option ==2:
            decoded = decode(encoded)
            print(f"\nThe encoded password is {encoded}, and the original password is {decoded}.")
        elif option == 3:
            exit()


if __name__ == "__main__":
    main()

# Worked with Michael
