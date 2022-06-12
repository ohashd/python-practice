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
#
# Runtime is O(VE) or O(V^3) when E is maximally populated.
# Works with negative weights and can detect negative cycles.

import sys

def bellman_ford_shortest_path(adjacency_list, start_node, end_node):
    num_nodes = len(adjacency_list)
    previous_node = [-1 for _ in range(num_nodes)]
    distances = [sys.maxsize for _ in range(num_nodes)]
    distances[start_node] = 0

    for _ in range(num_nodes-1):
        for edge_start, adjacency_dict in enumerate(adjacency_list):
            for edge_end, edge_weight in adjacency_dict.items():
                potential_new_weight = distances[edge_start] + edge_weight
                if potential_new_weight < distances[edge_end]:
                    distances[edge_end] = potential_new_weight
                    previous_node[edge_end] = edge_start

    # check for negative cycles
    for edge_start, adjacency_dict in enumerate(adjacency_list):
        for edge_end, edge_weight in adjacency_dict.items():
            potential_new_weight = distances[edge_start] + edge_weight
            if potential_new_weight < distances[edge_end]:
                raise Exception("Negative cycle found in graph.")

    # Print solution via back tracking
    if distances[end_node] < sys.maxsize:
        selected = [end_node]
        cur_node = end_node
        while cur_node != start_node:
            cur_node = previous_node[cur_node]
            selected.append(cur_node)
        selected.reverse()
        print(selected)

    return distances[end_node]


if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    num_nodes = int(input_lines[0])
    start_node, end_node = list(map(int, input_lines[1].split(" ")))
    adjacency_list = [{} for _ in range(num_nodes)]
    for edge_line in input_lines[2:]:
        edge_start, edge_end, weight = list(map(int, edge_line.split(" ")))
        adjacency_list[edge_start][edge_end] = weight

    soln = bellman_ford_shortest_path(adjacency_list, start_node, end_node)
    print(soln)

    # print(num_nodes)
    # print(start_node)
    # print(end_node)
    # print(nodes)
