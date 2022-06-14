# This program will find the cheapest path down the provided triangle.
#
# 1
# 2 3
# 5 5 1
# 4 4 2 7
#
# Sample solution: 1 -> 3 -> 1 -> 2 = 7
#
# Runtime is O(N) where N is the number of nodes in the triangular graph.

import sys
from copy import deepcopy

def triangle_shortest_path(triangle):
    if(len(triangle)==1):
        return triangle[0][0]

    if(len(triangle)==2):
        return min(triangle[1]) + triangle[0][0]
    
    shortest_path = deepcopy(triangle)
    # Populate the sides of the triangle
    for i_level, level in enumerate(triangle[1:],start=1):
        shortest_path[i_level][0] = level[0] + shortest_path[i_level - 1][0]
        shortest_path[i_level][-1] = level[-1] + shortest_path[i_level - 1][-1]
        for i_sub in range(1, len(level) - 1):
            shortest_path[i_level][i_sub] = min(shortest_path[i_level - 1][i_sub - 1:i_sub+1]) + level[i_sub]

    return min(shortest_path[-1])



if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    triangle = [list(map(int, line.split(" "))) for line in input_lines]
    soln = triangle_shortest_path(triangle)
    print(soln)
