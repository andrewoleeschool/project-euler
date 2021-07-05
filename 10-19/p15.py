# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

import numpy as np

n = 20

n += 1
grid = np.full((n, n), 1)

for i in range(1, n):
    for j in range(1, n):
        grid[i, j] = grid[i - 1, j] + grid[i, j - 1]

print(grid[n -1, n - 1])

# 137846528820