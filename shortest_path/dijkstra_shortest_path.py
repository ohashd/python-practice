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
# Runtime is O(V^2).
# Will not work when there are negative weights in the graph.
# Can optimize with a priority queue to store the remaining_nodes_distances.

from operator import itemgetter, attrgetter
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
from util.priority_queue import PriorityQueue

def dijkstra_shortest_path(adjacency_list, start_node, end_node):
    num_nodes = len(adjacency_list)
    previous_node = [-1 for _ in range(num_nodes)]
    rem_nodes_distances = PriorityQueue()
    rem_nodes_distances.insert(0, priority=0)
    for i in range(1, num_nodes):
        rem_nodes_distances.insert(i, priority=sys.maxsize)

    while rem_nodes_distances.length > 0 and rem_nodes_distances.min.priority != sys.maxsize:

        cur_node, cur_distance = attrgetter('item', 'priority')(rem_nodes_distances.pop_min())

        if cur_node == end_node:
            # Print solution via back tracking
            selected = [end_node]
            cur_node = end_node
            while cur_node != start_node:
                cur_node = previous_node[cur_node]
                selected.append(cur_node)
            selected.reverse()
            print(selected)
            return cur_distance

        for edge_end, weight in adjacency_list[cur_node].items():
            if not rem_nodes_distances.has_item(edge_end):
                continue
            potential_new_dist = cur_distance + weight
            if (potential_new_dist < rem_nodes_distances.get_priority(edge_end)):
                rem_nodes_distances.change_priority(edge_end, potential_new_dist)
                previous_node[edge_end] = cur_node

    return None



if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    num_nodes = int(input_lines[0])
    start_node, end_node = list(map(int, input_lines[1].split(" ")))
    adjacency_list = [{} for _ in range(num_nodes)]
    for edge_line in input_lines[2:]:
        edge_start, edge_end, weight = list(map(int, edge_line.split(" ")))
        adjacency_list[edge_start][edge_end] = weight

    soln = dijkstra_shortest_path(adjacency_list, start_node, end_node)
    print(soln)

    # print(num_nodes)
    # print(start_node)
    # print(end_node)
    # print(nodes)
