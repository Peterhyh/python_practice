string = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"

split_string = string.split(';')
split_string.pop()

first_row = []


filtered_row = []

for i in range(0, len(split_string)):
    split_index = split_string[i].split(':')
    first_row.append(split_index[1])
    filtered_row.append(split_index[0])

string = ''
for j in first_row:
    string += j + ' '

second_row = filtered_row[0].split(',')
third_row = filtered_row[1].split(',')


print(third_row)


# first_array = input_string.split(";")

# # first_array = ['5.0,100,5.5,101,6.0,102:L10', '5.0,99,5.5,100,6.0,101:L20', '']
# first_array.pop()
# # first_array = ['5.0,100,5.5,101,6.0,102:L10', '5.0,99,5.5,100,6.0,101:L20']

# output_lines = []

# second_array = first_array[0].split(":")
# # second_array = ['5.0,100,5.5,101,6.0,102', 'L10']
# third_array = second_array[0].split(",")
# # third_array = ['5.0', '100', '5.5', '101', '6.0', '102']

# for j in range(0, int(len(third_array)/2)+1):
#     output_lines.append("")
# # output_lines = ['']
# # output_lines = ['', '']
# # output_lines = ['', '', '']
# # output_lines = ['', '', '', '']
# # why divid by 2 and then add 1?

# for i in range(0, len(first_array)):
#     line = first_array[i].split(":")
#     # line =
#     # ['5.0,100,5.5,101,6.0,102', 'L10']
#     # ['5.0,99,5.5,100,6.0,101', 'L20']
#     output_lines[0] += "," + line[1]
#     # output_lines = [',L10,L20', '', '', '']

#     part_1 = line[0].split(",")
#     # part_1 =
#     # ['5.0', '100', '5.5', '101', '6.0', '102']
#     # ['5.0', '99', '5.5', '100', '6.0', '101']
#     cont = 0

#     for j in range(0, len(part_1)):
#         if not j % 2 and not i % 2:
#             output_lines[cont+1] += "," + part_1[j]
#             cont += 1
#             print(output_lines)
#             # output_lines = [',5.0']

# #         if j % 2 and not i % 2:
# #             output_lines[cont] += "," + part_1[j]

# #         if j % 2 and i % 2:
# #             cont += 1
# #             output_lines[cont] += "," + part_1[j]

# # for i in output_lines:
# #     print(i.replace(",", "   "))
