
# defining function of encryption
def encrypt(filename = None, key = None):
    if filename is None:
        filename = input("Give me the path of the file with extension:")
    if key is None:
        key = input("Give me a NUMBER as a key:")
    try:
        file = open(filename, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ int(key)

        file = open("Encrypted-" + filename, "wb")
        file.write(data)
        file.close()
    except FileNotFoundError as e:
        print(f"Error: {e}. Give me valid path:")
        encrypt(None, key)
    except ValueError as e:
        print(f"Error: {e}. Give me NUMBER as a key:")
        encrypt(filename, None)
    except:
        print("Unexpected Error!")
        encrypt(None, None)


# defining function of decryption
def decrypt(filename = None, key = None):
    if filename is None:
        filename = input("Give me the path of the encrypted file with extension:")
    if key is None:
        key = input("Give me a NUMBER as a key:")
    try:
        file = open(filename, "rb")
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, value in enumerate(data):
            data[index] = value ^ int(key)
        file = open(filename, "wb")
        file.write(data)
        file.close()
    except FileNotFoundError as e:
        print(f"Error: {e}. Give me valid path:")
        decrypt(None, key)
    except ValueError as e:
        print(f"Error: {e}. Give me NUMBER as a key:")
        decrypt(filename, None)
    except:
        print("Unexpected Error!")
        decrypt(None, None)


#calling the functions
def call_functions():
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("0. Quit")

    choice = ""
    while choice != 0:
        try:
            choice = int(input("Please select you option: "))
        except ValueError as e:
            print(f"Error: {e}. Give me NUMBER as option!")
            call_functions()
            break
        if choice == 1:
            encrypt()
        if choice == 2:
            decrypt()
        if choice == 0:
            break



