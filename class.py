""" class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player('Peter', 777)
player2 = Player('John', 316)

print('P1:', player1.name, 'hp:', player1.hp, 'score:', player1.score)
print('P2:', player2.name, 'hp:', player2.hp, 'score:', player2.score) """


""" class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, password):
        self.password = password
        print(self.username, 'password was changed to:', self.password, )


user1 = User('Peter', 'password123')
print(user1.username, user1.password)
user1.change_password('123password')
print(user1.username, user1.password) """


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.balance = 0

    def deposit(self):
        self.balance += float(input('Enter amount to deposit: $'))

    def withdraw(self):
        self.balance -= float(input('Enter amount to withdraw: $'))

    def check_balance(self):
        print('Current balance: $' + str(self.balance))


customer1 = Customer('Peter', 'password123')


while True:

    customer_selection = input(
        'Please select the following option:\n1) Check Balance\n2) Deposit\n3) Withdraw\n\n')

    if customer_selection == '1':
        customer1.check_balance()
    elif customer_selection == '2':
        customer1.deposit()
    elif customer_selection == '3':
        customer1.withdraw()
    else:
        print('Invalid selection!\n\nPlease try again...')
