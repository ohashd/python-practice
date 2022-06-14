# given a string, find the longest substring without repeating
# characters. e.g.
#
#   abcabcbb
#
# would return 3

import sys
from collections import defaultdict

def longest_substring(string):
    cur_longest = 0
    start_i = 0
    char_count = defaultdict(lambda: 0)

    for end_i, end_char in enumerate(string):
        
        char_count[end_char] += 1
        while char_count[end_char] > 1:
            start_char = string[start_i]
            char_count[start_char] -= 1
            start_i += 1
        
        potential_length = 1 + end_i - start_i
        cur_longest = max(cur_longest, potential_length)
    
    return cur_longest
        


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        print(longest_substring(line))