import numpy as np
from numpy.lib import polynomial

with open("input.txt") as f:
    lines = f.readlines()

data = np.array(list(map(int, lines[0].split(","))))

best_posistion = np.median(data)

print("Total fuel to reach: " + str((np.abs(data - best_posistion)).sum()))

# 7b


def run_sum(n):
    return sum(range(1, int(n) + 1))


def fuel_cost(posistion, data):
    return sum([run_sum(x) for x in np.abs(data - posistion)])


while True:
    up_posistion = best_posistion + 1
    down_posistion = best_posistion - 1
    old_fuel = fuel_cost(best_posistion, data)
    new_fuel_up = fuel_cost(up_posistion, data)
    new_fuel_down = fuel_cost(down_posistion, data)
    if (
        (old_fuel <= new_fuel_down)
        and (old_fuel <= new_fuel_up)
        and ((old_fuel < new_fuel_down) or (old_fuel < new_fuel_up))
    ):
        print(
            "\nBest position: "
            + str(best_posistion)
            + ". with total fuel cost of: "
            + str(old_fuel)
        )
        print(
            "\nUp would be:\nBest position:"
            + str(up_posistion)
            + ". with total fuel cost of: "
            + str(new_fuel_up)
        )
        print(
            "\nDown would be:\nBest position:"
            + str(down_posistion)
            + ". with total fuel cost of: "
            + str(new_fuel_down)
        )
        break
    else:
        best_posistion = up_posistion if (old_fuel > new_fuel_up) else down_posistion
