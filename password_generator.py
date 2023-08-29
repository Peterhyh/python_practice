import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print('PASSWORD GENERATOR')

character_length = int(input(
    'How many letters would you like in your password?\n'))

symbol_length = int(input('How many symbols would you like?\n'))

number_length = int(input('How many numbers would you like?\n'))

compile_password = []

for char in range(1, character_length + 1):
    random_index = random.randint(0, 51)
    compile_password.append(random.choice(letters))

for char in range(1, symbol_length + 1):
    random_index = random.randint(0, 9)
    compile_password.append(random.choice(symbols))

for char in range(1, number_length + 1):
    random_index = random.randint(0, 9)
    compile_password.append(random.choice(numbers))

random.shuffle(compile_password)
password_result = ''.join(compile_password)

print(f'\nYour generated password is:\n{password_result}\n')
