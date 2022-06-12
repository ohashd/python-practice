# Given a 2d grid of 1's (land) and 0's (water), return the number of islands

import sys

def index_2d(list, item):
    for y, sublist in enumerate(list):
        if item in sublist:
            return(y, sublist.index(item))
    return None

def num_islands(grid):
    num_rows = len(grid)
    num_columns = len(grid[0])
    # mark water as visited - we only need to visit land
    visited = [[1-grid[y][x] for x in range(num_columns)] for y in range(num_rows)]
    num_islands = 0

    # Breadth first search on a queue so we can avoid recursion.
    while index := index_2d(visited, 0):
        fifo_queue = [index]
        num_islands += 1
        while len(fifo_queue) > 0:
            cur_y, cur_x = fifo_queue.pop(0)
            visited[cur_y][cur_x] = 1

            for neighbor_y, neighbor_x in [\
                (cur_y - 1, cur_x),
                (cur_y + 1, cur_x),
                (cur_y, cur_x - 1),
                (cur_y, cur_x + 1)]:

                if neighbor_y >= 0 and neighbor_y < num_rows and \
                    neighbor_x >=0 and neighbor_x < num_columns and \
                    visited[neighbor_y][neighbor_x] == 0:

                    fifo_queue.append((neighbor_y, neighbor_x))


    return num_islands



if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    grid = [list(map(int, line.split(" "))) for line in input_lines]
    print(num_islands(grid))