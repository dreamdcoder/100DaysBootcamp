from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'attempts', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceaser(text, shift, direction):
    end_text = ''
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char not in alphabet:
            end_text += char
        else:
            idx = alphabet.index(char)
            new_idx = (idx + shift)
            end_text += alphabet[new_idx]

    print(f"result text is {end_text}")


# def encrypt(text, shift ,direction):
#     encrypted_text = []
#     for j in text:
#         idx = alphabet.index(j)
#         new_idx = (idx + shift) % 26
#         encrypted_text += alphabet[new_idx]
#     print(''.join(encrypted_text))
#
# def decrypt(text, shift):
#     decrypted_text = []
#     for j in text:
#         idx = alphabet.index(j)
#         new_idx = (idx - shift)
#         # if new_idx < 0:
#         #    new_idx += 26
#         decrypted_text += alphabet[new_idx]
#     print(''.join(decrypted_text))


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
if __name__ == "__main__":
    retry = 'yes'
    print(logo)
    while retry == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        ceaser(text=text, direction=direction, shift=shift)
        retry = input("Do you want to continue? type 'yes' or 'no'.\n").lower()
