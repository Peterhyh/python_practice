class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name():

    def change_pin():

    def change_password():


class BankUser:
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
