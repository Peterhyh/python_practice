""" class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player('Peter', 777)
player2 = Player('John', 316)

print('P1:', player1.name, 'hp:', player1.hp, 'score:', player1.score)
print('P2:', player2.name, 'hp:', player2.hp, 'score:', player2.score) """


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, password):
        self.password = password
        print(self.username, 'password was changed to:', self.password, )


user1 = User('Peter', 'password123')
print(user1.username, user1.password)
user1.change_password('123password')
print(user1.username, user1.password)
