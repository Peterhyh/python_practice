unsorted_list = [10, 23, 45, 14, 1, 5, 21]

# def bubble_sort(list):
# declare high index
# for in statement and pass in the high index value

high_index = len(unsorted_list) - 1

for i in range(high_index):
    for j in range(high_index):
        item = unsorted_list[j]
        next = unsorted_list[j + 1]

        if item > next:
            unsorted_list[j] = next
            unsorted_list[j + 1] = item

        print(unsorted_list, i, j)
