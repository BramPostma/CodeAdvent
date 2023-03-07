import numpy as np
from data import movement

speelveld_a = np.zeros((1000, 1000))
speelveld = np.zeros((1000, 1000))


def traceLine(vector, speelveld, speelveld_a):
    start_x = vector[0][0]
    end_x = vector[1][0]
    start_y = vector[0][1]
    end_y = vector[1][1]

    direction_x = 1 if start_x <= end_x else -1
    direction_y = 1 if start_y <= end_y else -1

    if (start_x == end_x) or (start_y == end_y):
        for x in range(start_x, end_x + direction_x, direction_x):
            for y in range(start_y, end_y + direction_y, direction_y):
                speelveld_a[y, x] = speelveld_a[y, x] + 1
                speelveld[y, x] = speelveld[y, x] + 1
    else:
        len_x = abs(end_x - start_x) + 1
        len_y = abs(end_y - start_y) + 1
        if len_x != len_y:
            raise ValueError()
        for i in range(len_x):
            y = start_y + (direction_y * i)
            x = start_x + (direction_x * i)
            speelveld[y, x] = speelveld[y, x] + 1
    return speelveld, speelveld_a


n_movements = len(movement)

for i in range(n_movements):
    speelveld, speelveld_a = traceLine(movement[i], speelveld, speelveld_a)

print((speelveld_a > 1 * 1).sum())
print((speelveld > 1 * 1).sum())
