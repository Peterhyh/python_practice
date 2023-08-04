def show_balance(balance):
    print('Current Balance: $' + str(balance))


def deposit(balance):
    deposit_amt = float(input('Enter amount to deposit: '))
    print('Current Balance: $' + str(balance + deposit_amt))
    return balance + float(deposit_amt)


def withdraw(balance):
    while True:
        withdraw_amt = float(input('Enter amount to withdraw: '))
        if withdraw_amt > balance:
            print('Insufficient funds!')
        elif withdraw_amt <= balance:
            new_balance = balance - withdraw_amt
            print('Current Balance: $' + str(new_balance))
            return new_balance


def logout(name):
    print('Goodbye', name.capitalize() + '!')
