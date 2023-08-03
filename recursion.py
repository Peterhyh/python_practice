def rFib(index):
    if index == 0:
        return 0
    elif index == 1 or index == 2:
        return 1
    else:
        return rFib(index - 1) + rFib(index - 2)
