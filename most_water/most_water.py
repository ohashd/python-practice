# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.
import sys

def most_water(walls):
    num_walls = len(walls)
    start_index = 0
    end_index = num_walls - 1
    max_capacity = 0
    while (start_index < end_index):
        start = walls[start_index]
        end = walls[end_index]
        capacity = min(end, start) * (end_index - start_index)
        if capacity > max_capacity:
            max_capacity = capacity
        if start > end:
            end_index -= 1
        else:
            start_index += 1
    
    return max_capacity


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        walls = list(map(int, line.split(" ")))
        print(most_water(walls))