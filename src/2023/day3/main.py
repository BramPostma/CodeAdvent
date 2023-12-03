import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text, is_numeric, len_of_int

text_list = read_text("day3/input.txt")

def get_first_number(input_string: str) -> (int, int):
    """ Get first number in a string and its starting index """
    for string_index, char in enumerate(input_string):
        if is_numeric(char):
            i = string_index
            try:
                while is_numeric(input_string[i]):
                    i = i+1
            except IndexError:
                pass
            return int(input_string[string_index:i]), string_index
    return 0, -1


def check_neighbors(current_row: str, index_start: int, length_num: int, row_above: str = None, 
                    row_below: str = None):
    """ Check if one of the neightbors is a symbol """
    start_index = max(0,(index_start-1))
    eind_index = min(len(current_row),(index_start+length_num+1))

    if check_row(current_row, [start_index, (eind_index-1)]):
        return True

    if row_above:
        if check_row(row_above,list(range(start_index,eind_index))):
            return True
    if row_below:
        if check_row(row_below,list(range(start_index,eind_index))):
            return True
    return False


def check_row(row_to_check: str, indexes = list[int]):
    """ Check if any of the indexes is a symbol"""
    for char_index in indexes:
        char = row_to_check[char_index]
        if (not is_numeric(char)) and (char != "."):
            return True
    return False


def find_number(current_row: str, index_start: int, row_above: str = None, row_below: str = None):
    """ Checks for number in string and if neighbors are symbols count towards total sum """
    if index_start >= (len(current_row)-1):
        return 0

    number, found_index = get_first_number(current_row[index_start:])
    if found_index<0:
        return 0

    num_index = index_start + found_index
    next_index = num_index + len_of_int(number)
    #print(f"Found number {number} at index {num_index} and next search is at {next_index}")
    if check_neighbors(current_row, num_index, len_of_int(number), row_above, row_below):
        return number + find_number(current_row, next_index, row_above, row_below)
    
    return find_number(current_row, next_index, row_above, row_below)


# Solution
sum_total = 0

for index, row in enumerate(text_list):
    if index == 0:
        sum_total = sum_total + find_number(row, 0, row_below=text_list[(index+1)])
    elif index == (len(text_list)-1):
        sum_total = sum_total + find_number(row, 0, row_above=text_list[(index-1)])
    else:
        sum_total = sum_total + find_number(row, 0, row_above=text_list[(index-1)], 
                                            row_below=text_list[(index+1)])

print(sum_total)