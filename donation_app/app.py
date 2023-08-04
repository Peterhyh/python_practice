from donation_pkg import homepage, user

database = {"admin": "password"}

donations = []

authorized_user = ""


while True:
    homepage.show_homepage()
    if authorized_user == "":
        print('\nYou must be logged in to donate.\n')
    if authorized_user != "":
        print('\nLogged in as:', authorized_user.capitalize(), '\n')

    user_input = input('Choose an option: ')

    if user_input == "1":
        authorized_user = user.login(database)
    elif user_input == "2":
        authorized_user = user.register(database)
        if authorized_user != '':
            while True:
                password = input('Enter password: ')
                if len(password) < 5:
                    print('Password must be at least 5 characters!')
                else:
                    database[authorized_user] = password
                    print('Username', authorized_user.capitalize(),
                          'successfully registered!')
                    break

    elif user_input == "3":
        if authorized_user == "":
            print('You are not logged in!')
        elif authorized_user != "":
            donation_string = homepage.donate(authorized_user)
            donations.append(donation_string)
    elif user_input == "4":
        homepage.show_donations(donations)
    elif user_input == "5":
        print("Goodbye", authorized_user)
        quit()
    else:
        print('Invalid selection\nTry again...')
