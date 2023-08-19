unsorted_list = [10, 23, 45, 14, 1, 5, 21]


high_index = len(unsorted_list) - 1


def bubble_sort(list):
    for i in range(high_index):
        for j in range(high_index):
            item = list[j]
            next = list[j + 1]

            if item > next:
                list[j] = next
                list[j + 1] = item

            print(list, i, j)


bubble_sort(unsorted_list)
