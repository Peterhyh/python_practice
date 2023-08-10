def linear_search(list, target):
    for x in range(len(list)):
        if list[x] == target:
            print('Found item in index:', x)
    print('Target is not in the list!')
    return -1


list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

linear_search(list, 74)
