import string


def create_shift(n):
    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        sub_letter = string.ascii_uppercase[(i + n) % alphabet_size]
        encoding[letter] = sub_letter
        decoding[sub_letter] = letter

    return encoding, decoding


def encode(message, sub):
    cipher = ''
    for i in message:
        if i in sub:
            cipher += sub[i]
        else:
            cipher += i

    return cipher


def decode(message, sub):
    return encode(message, sub)


def print_sub(sub):
    mapping = sorted(sub.items())
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)

    return "{}\n{}".format(alphabet_line, cipher_line)


if __name__ == '__main__':
    n = 1
    encoding, decoding = create_shift(n)
    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()
        if choice == '1':
            print("Encoding Table:")
            print(print_sub(encoding))
            print("Decoding Table:")
            print(print_sub(decoding))

        elif choice == '2':
            message = input("\nMessage to encode: ")
            print("Encoded Message: {}".format(
                encode(message.upper(), encoding)))

        elif choice == '3':
            message = input("\nMessage to decode: ")
            print("Decoded Message: {}".format(
                decode(message.upper(), decoding)))

        elif choice == '4':
            new_shift = input("\nNew shift (currently {}): ".format(n))
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception("Shift must be greater than 0")
            except ValueError:
                print("Shift {} is not a valid number.".format(new_shift))
            else:
                n = new_shift
                encoding, decoding = create_shift(n)

        elif choice == '5':
            print("Terminating. This program will self destruct in 5 seconds .\n")
            break

        else:
            print("Unknown option {}.".format(choice))
