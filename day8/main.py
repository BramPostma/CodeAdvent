import numpy as np

input = []

with open('input.txt') as f:
    for line in f:
        new_line = list(line.strip().split(' '))
        input = input + [new_line]


len_input = []
total_sum = 0

# 2(1), 3(7), 4(4), 7(8) elements(number)
for i in range(len(input)):

    new_line = [len(x) for x in input[i][-4:]]
    total_sum = total_sum + sum([x in (2,3,4,7) for x in new_line])
    len_input = len_input + [new_line]

print(total_sum)

# 8b

len_signals = []

# 2(1), 3(7), 4(4), 7(8) elements(number)
for i in range(len(input)):
    new_line = [len(x) for x in input[i][:-5]]
    len_signals = len_signals + [new_line]

def find_top_segment(input_layer):
    letters_two = [x for x in input_layer if len(x) == 2][0]
    letters_three = [x for x in input_layer if len(x) == 3][0]
    for letter in letters_three:
        if letter not in letters_two:
            return letter

def find_bottom_segment(input_layer):
    letters_four = [x for x in input_layer if len(x) == 4][0]
    letter_top = find_top_segment(input_layer)
    letter_total = letters_four+letter_top
    for number in input_layer:
        if (len(number) == 6):
            check = 0
            for letter in number:
                if letter in letter_total:
                    check += 1
                else:
                    bottom_segment = letter
            if check == 5:
                return bottom_segment

def find_middle_segment(input_layer):
    letters_two = [x for x in input_layer if len(x) == 2][0]
    letter_top = find_top_segment(input_layer)
    letter_bottom = find_bottom_segment(input_layer)
    letter_total = letters_two+letter_top+letter_bottom
    for number in input_layer:
        if (len(number) == 5):
            check = 0
            for letter in number:
                if letter in letter_total:
                    check += 1
                else:
                    middle_segment = letter
            if check == 4:
                return middle_segment

def find_bottom_left_segment(input_layer):
    letters_four = [x for x in input_layer if len(x) == 4][0]
    letter_top = find_top_segment(input_layer)
    letter_bottom = find_bottom_segment(input_layer)
    letter_total = letters_four+letter_top+letter_bottom
    for number in input_layer:
        if (len(number) == 7):
            for letter in number:
                if letter not in letter_total:
                    return(letter)

def find_top_left_segment(input_layer):
    letters_two = [x for x in input_layer if len(x) == 2][0]
    letter_top = find_top_segment(input_layer)
    letter_bottom = find_bottom_segment(input_layer)
    letter_bottom_left = find_bottom_left_segment(input_layer)
    letter_total = letters_two+letter_top+letter_bottom+letter_bottom_left
    for number in input_layer:
        if (len(number) == 6):
            check = 0
            for letter in number:
                if letter in letter_total:
                    check += 1
                else:
                    top_left_segment = letter
            if check == 5:
                return top_left_segment

def find_top_right_segment(input_layer):
    letter_middle = find_middle_segment(input_layer)
    letter_top = find_top_segment(input_layer)
    letter_bottom = find_bottom_segment(input_layer)
    letter_bottom_left = find_bottom_left_segment(input_layer)
    letter_total = letter_middle+letter_top+letter_bottom+letter_bottom_left
    for number in input_layer:
        if (len(number) == 5):
            check = 0
            for letter in number:
                if letter in letter_total:
                    check += 1
                else:
                    top_right_segment = letter
            if check == 4:
                return top_right_segment

def find_bottom_right_segment(input_layer):
    letters_two = [x for x in input_layer if len(x) == 2][0]
    letter_top_right = find_top_right_segment(input_layer)
    for letter in letters_two:
        if letter != letter_top_right:
            return letter

def translator(input_layer):
    return [find_top_segment(input_layer),find_top_left_segment(input_layer),find_top_right_segment(input_layer),find_middle_segment(input_layer),find_bottom_left_segment(input_layer),find_bottom_right_segment(input_layer),find_bottom_segment(input_layer)]

def decoder(translation,letters):
    nummers = []
    for letter in letters:
        nummers = nummers + [translation.index(letter)+1]
    let_to_num = [[1,2,3,5,6,7],[3,6],[1,3,4,5,7],[1,3,4,6,7],[2,3,4,6],[1,2,4,6,7],[1,2,4,5,6,7],[1,3,6],[1,2,3,4,5,6,7],[1,2,3,4,6,7]] # Een 1 bestaat uit segment 3 en 6 die licht geven
    i=0
    for let in let_to_num:
        if set(nummers) == set(let):
            return i
        i +=1
    raise ValueError()

def total_number(input_layer):
    total = ''
    translation = translator(input_layer[:-5])
    for letters in input_layer[-4:]:
        total = total + str(decoder(translation,letters))
    return(int(total))

total_sum = 0
for row in input:
    total_sum += total_number(row)

print(total_sum)