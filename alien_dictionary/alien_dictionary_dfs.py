# Input is a list of words in a different language where
# the alphabet has a different order. Return the characters appearing
# in the input in the order of the different language. If
# the input was not sorted i.e. ('z', 'x', 'z'), return None.

# This solution uses a depth first search (DFS) to do a topological
# sort. Runtime is x since there are a limited number of characters
# the topological sort can be considered O(1).

# With an unlimited number of characters (K), the runtime would
# be x

from operator import itemgetter
from functools import reduce
import sys

def alien_dictionary_dfs(list_of_words):

    directed_edges = {}
    seen = set()

    for lastword, word in zip(list_of_words[:-1],list_of_words[1:]):
        lastword_len = len(lastword)
        word_len = len(word)
        seen = seen.union(word, lastword)
        num_comparisons = min(lastword_len, word_len)
        for i in range(num_comparisons):
            lastword_char = lastword[i]
            word_char = word[i]

            if lastword_char == word_char:
                continue

            # Check if this edge exists already
            if (lastword_char in directed_edges and word_char in directed_edges[lastword_char]):
                continue

            # Record outgoing edge
            if (lastword_char not in directed_edges):
                directed_edges[lastword_char] = []
            directed_edges[lastword_char].append(word_char)

    # DFS to sort graph topologically
    markers = {node: 0 for node in seen}
    result = ""

    while True:
        nodes_left = list(filter(lambda item: item[1]==0, markers.items()))
        if len(nodes_left) == 0:
            break
        to_search = [(nodes_left[0][0], False)]
        while(len(to_search)>0):
            (cur_node, done_processing) = to_search.pop()
            if done_processing:
                markers[cur_node] = 2
                result = cur_node + result
            else:
                # If already done visiting this node
                if markers[cur_node] == 2:
                    continue

                # If temporarily marked (cycle, no solution)
                if markers[cur_node] == 1:
                    return None

                # Mark temporarily
                markers[cur_node] = 1

                # Add marker for this node so we can know when all it's children
                # have been visited on the stack. Then add all children to stack.
                to_search.append((cur_node, True))
                if cur_node in directed_edges:
                    children = directed_edges[cur_node]
                    to_search.extend([(child, False) for child in children])

    return result


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    print(alien_dictionary_dfs(input_lines))
