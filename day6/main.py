import numpy as np
from numpy.lib import polynomial

with open("input.txt") as f:
    lines = f.readlines()

population = np.array(list(map(int, lines[0].split(","))))

count_arr = np.bincount(population)
amounts = np.append(count_arr, np.array([0, 0, 0]))

overgangs_matrix = np.eye(8)
top_row = [0, 0, 0, 0, 0, 0, 1, 0]
overgangs_matrix = np.vstack([top_row, overgangs_matrix])
last_column = np.eye(9, 1)
overgangs_matrix = np.hstack([overgangs_matrix, last_column])


def make_babies(population):
    n_babies = sum(population == 0)
    babies = np.array(
        [9] * n_babies
    )  # baby gaat hierna meteen ouder worden naar 8 dagen
    return np.append(population, babies)


def get_old(population):
    population = population - 1
    overaged = population == -1
    population[overaged] = 6
    return population


def cycle(population):
    population = make_babies(population)
    population = get_old(population)
    return population


for i in range(80):
    population = cycle(population)

print(population.size)

int_array = population.astype(int)
count_arr = np.bincount(int_array)
print(count_arr)

# 6b

for i in range(256):
    amounts = np.matmul(amounts, overgangs_matrix)

print(amounts)
print(amounts.sum())
