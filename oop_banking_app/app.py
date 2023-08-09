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
        print('Your current balance is: $' + str(self.balance))

    def withdraw(self):
        withdraw_amount = input('How much would you like to withdraw? ')
        self.balance -= float(withdraw_amount)
        print('You withdrawed $' + str(withdraw_amount))
        print('Your current balance is: $' + str(self.balance))

    def transfer_money(self):
        user_pin = input("Enter the reciepiant's PIN number? ")
        transfer_amt = input('How much would you like to transfer? ')

    def request_money(self):
        request_amt = input('How much would you like to request? ')


peter = BankUser('Peter', '1234', 'pass123')
