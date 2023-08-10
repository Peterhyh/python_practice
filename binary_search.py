def binary_search(list, target):
    lower_index = 0
    upper_index = len(list) - 1

    while lower_index <= upper_index:
        pivot = (lower_index + upper_index) // 2
        pivot_value = list[pivot]

        if pivot_value == target:
            print('The target is at index:', pivot)
            return pivot
        if pivot_value > target:
            upper_index = pivot - 1
        else:
            lower_index = pivot + 1


list = [1, 2, 3, 4, 5, 6, 7]

binary_search(list, 7)
