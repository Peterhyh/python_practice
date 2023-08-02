power = pow(10, 10)
print(power)


def change_power(x, y):
    global power
    power = x + y


change_power(3, 4)
print(power)
