class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        self.name = input('Enter a name: ')

    def change_pin(self):
        self.pin = input('Enter a pin: ')

    def change_password(self):
        self.password = input('Enter a password: ')


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print('Your current balance is:', self.balance)

    def deposit(self):
        deposit_amount = input('How much would you like to deposit? ')
        self.balance += float(deposit_amount)
        print('You deposited $' + str(deposit_amount))
        print('Your current balance is: $' + str(self.balance), '\n')

    def withdraw(self):
        while True:
            withdraw_amount = input('How much would you like to withdraw? ')
            balance = self.balance - float(withdraw_amount)
            if balance >= 0:
                break
            else:
                print(self.name, 'does have enough to withdraw $' + withdraw_amount)
        self.balance -= float(withdraw_amount)
        print('You withdrawed $' + str(withdraw_amount))
        print('Your current balance is: $' + str(self.balance))

    def transfer_money(self, receiving_user):
        while True:
            transfer_amt = input('How much would you like to transfer? ')
            balance = self.balance - float(transfer_amt)

            if balance >= 0:
                print('You are transferring $' +
                      transfer_amt, 'to', receiving_user.name)
                print('Authentication required')
                break
            else:
                print("Unable to transfer amount.\nTransfer amount is more than " +
                      self.name.capitalize() + "'s balance!")

        while True:
            pin = input('Enter your PIN to confirm transfer: ')
            if pin == self.pin:
                print('Transfer authorized!')
                self.balance -= float(transfer_amt)
                receiving_user.balance += float(transfer_amt)
                print('Transferring $' + transfer_amt, 'to',
                      receiving_user.name.capitalize())
                break
            else:
                print('Your PIN was incorrect!\nPlease try again...')

    def request_money(self, other_user):
        while True:
            requested_amt = float(
                input('How much would you like to request from ' + other_user.name + '?'))
            balance = other_user.balance - requested_amt
            if balance >= 0:
                break
            else:
                print("Unable to withdraw amount.\nWithdraw amount is more than " +
                      other_user.name.capitalize() + "'s balance!")

        print('You are requesting $' + str(requested_amt),
              'from', other_user.name.capitalize() + '? ')
        print('User authentication is required...')

        while True:
            pin = input("Enter " + other_user.name.capitalize() + "'s PIN: ")
            password = input('Enter your password: ')
            if pin == other_user.pin and password == self.password:
                other_user.balance -= requested_amt
                self.balance += requested_amt
                print('Request authorized')
                print(other_user.name.capitalize(),
                      'sent $' + str(requested_amt))
                break
            else:
                print('Incorrect PIN and/or password.\nPlease try again...')


bankUser = BankUser('Peter', '1234', 'pass123')
bankUser2 = BankUser('Trinh', '321', 'word123')


# bankUser.deposit()
print(bankUser2.name.capitalize(),
      'has an account balance of: $' + str(bankUser2.balance))
print(bankUser.name.capitalize(),
      'has an account balance of: $' + str(bankUser.balance))

bankUser2.deposit()
bankUser2.withdraw()

# bankUser.transfer_money(bankUser2)


# bankUser2.request_money(bankUser)

print(bankUser2.name.capitalize(),
      'has an account balance of: $' + str(bankUser2.balance))
print(bankUser.name.capitalize(),
      'has an account balance of: $' + str(bankUser.balance))
