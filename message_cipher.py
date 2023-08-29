

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while True:
    user_selection = input('1) Decrypt\n2) Encrypt\n').lower()

    def encrypt(plain_text, shift_number):
        encrypted_text = []
        for letter in plain_text:
            if letter not in letters:
                encrypted_text.append(letter)
            else:
                old_index = letters.index(letter)
                new_index = old_index + shift_number
                encrypted_text.append(letters[new_index])

        new_text = ''.join(encrypted_text)

        print(f'Your encrypted word is:\n{new_text}')

    def decrypt(texts, shifts):
        decryted_text = []
        for letter in texts:
            if letter not in letters:
                decryted_text.append(letter)
            else:
                old_index = letters.index(letter)
                new_index = old_index - shifts
                decryted_text.append(letters[new_index])
        new_text = ''.join(decryted_text)
        print(f'Decrypted text:\n{new_text}')

    if user_selection == '2' or user_selection == 'encrypt':

        user_shift = int(input('Enter the shift:\n'))

        user_text = input('Enter in what you would like to encrypt.\n').lower()

        encrypt(user_text, user_shift)
        break

    elif user_selection == '1' or user_selection == 'decrypt':

        user_text = input('Enter in text to decrypt...\n')

        user_shift = int(input('Enter the shift:\n'))

        decrypt(user_text, user_shift)
        break

    else:
        print('Invalid selection.')
