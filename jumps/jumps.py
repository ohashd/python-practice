# given an array of numbers>0 where each element represents
# the number of indices you can jump forward,
# return the minimum number of jumps required to get to the end
# of the array
# Assumes a solution is always possible

import sys

def jumps(arr):
    num_jumps = farthest = current = 0
    for i, elem in enumerate(arr):
        farthest = max(farthest, i+elem)
        if i == current:
            current = farthest
            num_jumps += 1
            if current >= len(arr)-1:
                break

    return num_jumps


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        arr = list(map(int, line.split(" ")))
        print(jumps(arr))