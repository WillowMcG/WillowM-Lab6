

def encode(password):
    encoded = ""
    for char in password:
        char = int(char)
        char = char + 3
        char = str(char)
        encoded += char
    return encoded


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
        print("Your password has been encoded and stored!")

    elif option == 3:
        exit()

# Worked with Michael