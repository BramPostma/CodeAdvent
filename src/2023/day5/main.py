import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text, is_numeric, len_of_int

text_seeds = read_text("day5/input_seeds.txt")
text_map = read_text("day5/input_map.txt")