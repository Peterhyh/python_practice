def login(database):
    username = input('\nEnter username: ').lower()
    password = input('Enter password: ')

    if username in database and database[username] == password:
        print("\nWelcome back", username.capitalize() + '!\n')
        return username
    else:
        print('\nInvalid Credentials!\n\nPlease try again...\n\n')
        return ''


def register(database):

    username = input('Enter username: ').lower()

    if username in database:
        print('Username already exists!')
        return ''
    elif len(username) <= 0 or len(username) > 10:
        print('Username must be at least 1 to 10 characters!')
        return ''
    else:
        return username
