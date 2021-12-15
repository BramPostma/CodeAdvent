import numpy as np

input = []

with open('input.txt') as f:
    for line in f:
        new_line = list(line.strip().split(' '))
        input = input + [new_line]

input_array = np.array(input)