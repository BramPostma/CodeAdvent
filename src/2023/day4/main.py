import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text, is_numeric, len_of_int

text_list = read_text("day4/input.txt")