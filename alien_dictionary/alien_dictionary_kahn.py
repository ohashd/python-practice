# Input is a list of words in a different language where
# the alphabet has a different order. Return the characters appearing
# in the input in the order of the different language. If
# the input was not sorted i.e. ('z', 'x', 'z'), return None.

# This solution uses kahns algorithm for a topological sort.
# Runtime is O(N) since there are a limited number of characters
# the topological sort can be considered O(1).

# With an unlimited number of characters (K), the runtime would
# be O(N + K^2) since topsort runs in O(V+E) and E could potentially
# be O(V^2).

from operator import itemgetter
from functools import reduce
import sys

def alien_dictionary_kahn(list_of_words):

    directed_edges = {}
    rev_directed_edges = {}
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
            if (word_char in rev_directed_edges and lastword_char in rev_directed_edges[word_char]):
                continue

            # Record outgoing edge
            if (lastword_char not in directed_edges):
                directed_edges[lastword_char] = []
            directed_edges[lastword_char].append(word_char)

            # Record incoming edge
            if (word_char not in rev_directed_edges):
                rev_directed_edges[word_char] = []
            rev_directed_edges[word_char].append(lastword_char)

    # Kahns algorithm to topological sort the graph
    all_nodes = seen
    fn_no_incoming_nodes = lambda x: x not in rev_directed_edges or len(rev_directed_edges[x])==0
    no_incoming_edges_nodes = list(filter(fn_no_incoming_nodes, all_nodes))
    ordered_nodes = []

    # While there are nodes with no incoming edges
    while len(no_incoming_edges_nodes)>0:
        cur_node = no_incoming_edges_nodes.pop()
        ordered_nodes.append(cur_node)
        if cur_node not in directed_edges:
            continue

        # Remove all edges outgoing from the node (remove not optimal here)
        for end_node in directed_edges[cur_node]:
            rev_directed_edges[end_node].remove(cur_node)
            if len(rev_directed_edges[end_node]) == 0:
                no_incoming_edges_nodes.append(end_node)

    num_edges_remaining = reduce(lambda acc, value: acc+len(value), rev_directed_edges.values(), 0)

    if num_edges_remaining > 0:
        return None

    return "".join(ordered_nodes)




if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    print(alien_dictionary_kahn(input_lines))
