# This program will find the shortest path between the two nodes
# in a weighted DAG. The input will start with a line that specifies
# the number of nodes in the total graph. It is followed by a line
# that specifies the start and the end node. The remaining lines
# each specify a directed edge with a weight. e.g.
#
# 3
# 0 2
# 0 1 1
# 1 2 1
# 0 2 3
#
# Specifies a weighted DAG with 3 nodes where node 0 and 1 are connected
# with an edge of weight 1, node 1 and 2 are connected with a weight of 1,
# and node 0 and 2 are connected with a weight of 3. The shortest path
# is 0->1->2.

# Runtime is O(VE) or O(V^3) when E is maximally populated (to n(n-1)/2).
# Will also not work if there are any cycles in the graph.

import sys

def bruteforce_shortest_path(adjacency_list, start_node, end_node):
    if start_node == end_node:
        return 0
    candidates = [
        weight + bruteforce_shortest_path(adjacency_list, node_candidate, end_node)
        for node_candidate, weight in adjacency_list[start_node].items()
    ]
    if len(candidates) == 0:
        return sys.maxsize
    return min(candidates)

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    num_nodes = int(input_lines[0])
    start_node, end_node = list(map(int, input_lines[1].split(" ")))
    adjacency_list = [{} for _ in range(num_nodes)]
    for edge_line in input_lines[2:]:
        edge_start, edge_end, weight = list(map(int, edge_line.split(" ")))
        adjacency_list[edge_start][edge_end] = weight

    soln = bruteforce_shortest_path(adjacency_list, start_node, end_node)
    print(soln)

    # print(num_nodes)
    # print(start_node)
    # print(end_node)
    # print(nodes)
