import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_dir + "/..")

from util.general import read_text, is_numeric

text_list = read_text("day2/input.txt")


def get_color(draw_output: str, color_name: str):
    """ Based on a single draw and a color name, returns the amount of cubes present of that color """
    if (draw_output.find(color_name)) >= 0:
        number = draw_output[0]
        i = 1
        while is_numeric(draw_output[i]):
            number = number + draw_output[i]
            i = i + 1
        return int(number)
    return 0


def process_game_draws(game_draws: str, index: int) -> (int,int,int):
    """ Processes the draws of a single game and returns the index if its valid """
    max_red = 0
    max_green = 0
    max_blue = 0
    for single_draw in game_draws.split(";"):
        for single_color in single_draw.split(","):
            single_color_stripped = single_color.strip()
            max_red = max(max_red,get_color(single_color_stripped,"red"))
            max_green = max(max_green,get_color(single_color_stripped,"green"))
            max_blue = max(max_blue,get_color(single_color_stripped,"blue"))
    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        return index
    return 0

def process_game(game_outcome: str):
    """ Returns index of game if correct amount of cubes are present based on strings with all game info"""
    split_game_outcome = game_outcome.split(": ")
    game_index = int((split_game_outcome[0]).split(" ")[1])
    game_draws = split_game_outcome[1]
    return process_game_draws(game_draws=game_draws, index=game_index)

print(sum([process_game(x) for x in text_list]))
