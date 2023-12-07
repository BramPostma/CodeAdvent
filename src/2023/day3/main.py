import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text, is_numeric, len_of_int
from day3.day3_util import *

text_list = read_text("day3/input.txt")

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


def check_neighbors_stars(current_row: str, index_star: int, row_above: str = None, 
                          row_below: str = None):
    """ Check if one of the neightbors is a symbol """
    a,b = check_star_row(current_row,index_star)
    c,d,e,f = (0,0,0,0)

    if row_above:
        c,d = check_star_row(row_above,index_star)
        if is_numeric(row_above[index_star]):
            num_out = row_above[index_star]
            if int(c) > -1:
                num_out = c + num_out
            if int(d) > -1:
                num_out = num_out + d
            c, d = (int(num_out), 0)

    if row_below:
        e,f = check_star_row(row_below,index_star)
        if is_numeric(row_below[index_star]):
            num_out = row_below[index_star]
            if int(e) >= 0:
                num_out = e + num_out
            if int(f) >= 0:
                num_out = num_out + f
            e, f = (int(num_out), 0)
    return (int(a),int(b),int(c),int(d),int(e),int(f))


def check_star_row(row_to_check: str, index_star: int) -> (str, str):
    """ check what is before and after a star """
    a, b = ("-1","-1")
    num_before, index_before = get_first_number(row_to_check[:index_star][::-1], True, True)
    if index_before == 0:
        a = num_before
    num_after, index_after = get_first_number(row_to_check[(index_star+1):], False, True)
    if index_after == 0:
        b = num_after
    return a,b


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


def find_star(current_row: str, index_start: int, row_above: str = None, row_below: str = None):
    """ Checks for number in string and if neighbors are symbols count towards total sum """
    len_row = len(current_row)
    
    if index_start >= (len_row-1):
        return 0

    found_index = get_first_star(current_row[index_start:])
    if found_index<0:
        return 0

    star_index = index_start + found_index
    next_index = star_index + 1

    outputs =  check_neighbors_stars(current_row, star_index, row_above, row_below)
    greater_than_zero = [arg for arg in outputs if arg > 0]
    if len(greater_than_zero) == 2:
        return (greater_than_zero[0] * greater_than_zero[1]) + find_star(current_row, next_index,
                                                                         row_above, row_below)
    return find_star(current_row, next_index, row_above, row_below)


# Solution
sum_total = 0
sum_total_gear = 0

for index, row in enumerate(text_list):
    if index == 0:
        sum_total = sum_total + find_number(row, 0, row_below=text_list[(index+1)])
        sum_total_gear = sum_total_gear + find_star(row, 0, row_below=text_list[(index+1)])
    elif index == (len(text_list)-1):
        sum_total = sum_total + find_number(row, 0, row_above=text_list[(index-1)])
        sum_total_gear = sum_total_gear + find_star(row, 0, row_above=text_list[(index-1)])
    else:
        sum_total = sum_total + find_number(row, 0, row_above=text_list[(index-1)],
                                            row_below=text_list[(index+1)])
        sum_total_gear = sum_total_gear + find_star(row, 0, row_above=text_list[(index-1)],
                                            row_below=text_list[(index+1)])

print(f"{sum_total} and {sum_total_gear}")
