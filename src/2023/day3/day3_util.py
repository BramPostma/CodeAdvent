""" Generic funcs needed for day 2"""

from util.general import is_numeric

def get_first_number(input_string: str, reverse: bool=False, string_output: bool=False):
    """ Get first number in a string and its starting index """
    for string_index, char in enumerate(input_string):
        if is_numeric(char):
            i = string_index
            try:
                while is_numeric(input_string[i]):
                    i = i+1
            except IndexError:
                pass
            output = input_string[string_index:i]
            if reverse:
                output = reverse_number(output)
            if string_output:
                return str(output), string_index
            return int(output), string_index
    return 0, -1

def reverse_number(input_number: int) -> int:
    """ Convert the input number to a string and reverse it """
    reversed_str = str(input_number)[::-1]

    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)

    return reversed_number

def get_first_star(input_string: str) -> int:
    """ Get the index of the first star in a string """
    return input_string.find("*")

def get_first_non_digit(input_string: str) -> (int, int):
    """ Get index of the first non number in a string """
    for string_index, char in enumerate(input_string):
        if not is_numeric(char):
            return string_index
    return 0, -1
