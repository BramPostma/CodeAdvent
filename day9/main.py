import numpy as np

input: list = []

with open("input.txt") as f:
    for line in f:
        new_line = list(line.strip().split()[0])
        input = input + [[int(x) for x in new_line]]

input = np.array(input)
lowpoints = np.array([[0] * len(input[0])] * len(input))


def check_list(row: list):
    return_list: list = []
    return_list += [(True if row[0] < row[1] else False)]
    for i in range(1, (len(row) - 1)):
        return_list += [
            (True if (row[i] < row[i + 1] and row[i] < row[i - 1]) else False)
        ]
    return_list += [(True if row[(len(row) - 1)] < row[(len(row) - 2)] else False)]
    return return_list


first_col = [i[0] for i in input]

row_results = []
for i in range(len(input)):
    row_results += [check_list(input[i])]


column_results = []
for i in range(len(input[0])):
    column_results += [check_list([rows[i] for rows in input])]


for y in range(len(input)):
    for x in range(len(input[0])):
        lowpoints[y][x] = (row_results[y][x] * column_results[x][y]) * 1

# 9a
np.multiply(input, lowpoints).sum() + lowpoints.sum()


# 9b
