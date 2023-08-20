unsorted_list = [10, 23, 45, 14, 1, 5, 21]


high_index = len(unsorted_list) - 1


def bubble_sort(list):
    for i in range(high_index):
        for x in range(high_index):
            item = list[x]
            next = list[x + 1]

            if item > next:
                list[x] = next
                list[x + 1] = item

            print(list, i, x)


bubble_sort(unsorted_list)
