import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text

text_list = read_text("day1/input.txt")

numbers_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}


def written_number(input_string: str) -> str:
    """ Func to check if string starts with a written digit """
    if input_string[:3] in ["one", "two", "six"]:
        return input_string[:3]
    elif input_string[:4] in ["four", "five", "nine"]:
        return input_string[:4]
    elif input_string[:5] in ["three", "seven", "eight"]:
        return input_string[:5]
    return ""


def find_first_digit(input_string: str) -> int:    
    """ Func to find the first written or numeric digit in a string """
    
    for index, char in enumerate(input_string):
        if char.isdigit():
            return char
        elif len(found_number := written_number(input_string[index:])) > 0:
            return numbers_dict[found_number]
    raise TypeError("no digit in string")


def find_last_digit(input_string: str) -> int:
    """ Func to find the last written or numeric digit in a string """
    reverse_string = input_string[::-1]

    for index, char in enumerate(reverse_string):
        if char.isdigit():
            return char
        elif len(found_number := written_number(input_string[(len(input_string)-index-1):])) > 0:
            return numbers_dict[found_number]
    raise TypeError("no digit in string")



def process_input(input_string: str) -> int:
    first_int = find_first_digit(input_string)
    last_int = find_last_digit(input_string)
    return int(str(first_int) + str(last_int))

print(sum([process_input(x) for x in text_list]))