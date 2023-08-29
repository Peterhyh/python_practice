import random


while True:

    random_num = random.randint(0, 1)

    user_input = input('Start?\n1) yes\n2) no\n')
    if user_input == 'yes' or user_input == '1':
        if random_num == 0:
            print('\nHead!\n')
        else:
            print("\nTail!\n")
    elif user_input == 'no' or user_input == '2':
        print('Goodbye!')
        break
    else:
        print('Please select a valid choice.\n')
