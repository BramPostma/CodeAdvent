import numpy as np
from numpy.lib import polynomial

with open('input.txt') as f:
    lines = f.readlines()

population = np.array(list(map(int,lines[0].split(','))))

#with open('the-zen-of-python.txt') as f:
#    for line in f:
#        print(line)

def make_babies(population):
    n_babies = sum(population==0)
    babies = np.array([9]*n_babies) # baby gaat hierna meteen ouder worden naar 8 dagen
    return np.append(population,babies)

def get_old(population):
    population = population-1
    overaged = (population==-1)
    population[overaged] = 6
    return population

def cycle(population):
    population = make_babies(population)
    population = get_old(population)
    return population

for i in range(80):
    population = cycle(population)

print(population.size)