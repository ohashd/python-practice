# Given a grid of integers, find the path from top left to bottom right
# with the minimum total sum. Path can only proceed right and down.

import sys

def min_path_sum(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])
    min_dists = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    min_dists[0][0] = grid[0][0]

    for y in range(1, num_rows):
        min_dists[y][0] = min_dists[y - 1][0] + grid[y][0]
    for x in range(1, num_columns):
        min_dists[0][x] = min_dists[0][x - 1] + grid [0][x]
    
    for y in range(1, num_rows):
        for x in range(1, num_columns):
            min_dists[y][x] = min(min_dists[y-1][x], min_dists[y][x-1]) + grid[y][x]

    return min_dists[-1][-1]



if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    grid = [list(map(int, line.split(" "))) for line in input_lines]
    print(min_path_sum(grid))
