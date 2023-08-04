from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + str(name.capitalize()))
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")

balance = 0

while True:
    name = input('Enter name to register: ')
    if len(name) > 10 or len(name) < 1:
        print('Name must be 1 to 10 characters')
    elif len(name) <= 10 and len(name) >= 1:
        break

while True:
    pin = input('Enter PIN: ')
    if len(pin) > 4 or len(pin) < 4:
        print('PIN must be 4 characters')
    elif len(pin) == 4:
        break


print(name, 'has been registered with a starting balance of $' + str(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")

    name_to_validate = input('Enter name: ')
    pin_to_validate = input('Enter PIN: ')

    if name_to_validate != name or pin_to_validate != pin:
        print('Invalid credentials!')
    if name_to_validate == name and pin_to_validate == pin:
        print('Login successful!')
        break

while True:
    atm_menu(name_to_validate)
    option = input('Choose an option: ')
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
    elif option == '3':
        balance = account.withdraw(balance)
    elif option == '4':
        account.logout(name_to_validate)
        quit()
    else:
        print('Invalid option!')
