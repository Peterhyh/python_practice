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
        withdraw_amount = input('How much would you like to withdraw? ')
        self.balance -= float(withdraw_amount)
        print('You withdrawed $' + str(withdraw_amount))
        print('Your current balance is: $' + str(self.balance))

    def transfer_money(self, receiving_user):
        transfer_amt = input('How much would you like to transfer? ')
        print('You are transferring $' + transfer_amt, 'to', receiving_user.name)
        print('Authentication required')

        while True:
            pin = input('Enter your PIN to confirm transfer: ')
            if pin == self.pin:
                print('Transfer authorized!')
                self.balance -= float(transfer_amt)
                receiving_user.balance += float(transfer_amt)
                print('Transferring $' + pin, 'to',
                      receiving_user.name.capitalize())
                break
            else:
                print('Your PIN was incorrect!\nPlease try again...')

    def request_money(self, other_user):
        requested_amt = float(
            input('How much would you like to request from ' + other_user.name + '?'))
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


bankUser.deposit()
print(bankUser2.name.capitalize(),
      'has an account balance of: $' + str(bankUser2.balance))
print(bankUser.name.capitalize(),
      'has an account balance of: $' + str(bankUser.balance))

# bankUser.transfer_money(bankUser2)
# print(bankUser2.name.capitalize(), 'balance is: $' + str(bankUser2.balance))
# print(bankUser.name.capitalize(), 'balance is: $' + str(bankUser.balance))


bankUser2.request_money(bankUser)

print(bankUser2.name.capitalize(),
      'has an account balance of: $' + str(bankUser2.balance))
print(bankUser.name.capitalize(),
      'has an account balance of: $' + str(bankUser.balance))
