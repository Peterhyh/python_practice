input_string = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"

first_array = input_string.split(";")
first_array.pop()

output_lines = []

second_array = first_array[0].split(":")
third_array = second_array[0].split(",")


for j in range(0, int(len(third_array)/2)+1):
    output_lines.append("")


for i in range(0, len(first_array)):
    line = first_array[i].split(":")
    output_lines[0] += "," + line[1]

    part_1 = line[0].split(",")
    cont = 0

    for j in range(0, len(part_1)):
        if not j % 2 and not i % 2:
            output_lines[cont+1] += "," + part_1[j]
            cont += 1

        if j % 2 and not i % 2:
            output_lines[cont] += "," + part_1[j]

        if j % 2 and i % 2:
            cont += 1
            output_lines[cont] += "," + part_1[j]

for i in output_lines:
    print(i.replace(",", "   "))
