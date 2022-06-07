# Input starts with a single line defining the total
# weight the backpack is capable of carrying. It is followed
# by a series lines that each specify a weight and value for
# an item. The goal is to find the set of items that fit in the
# bag that maximize value.

import sys

class DPMatrix:
    def __init__(self, backpack_weight, num_items):
        self.dp_matrix = [[0 for _ in range(num_items)] for _ in range(backpack_weight)]

    def get(self, weight, item):
        if (weight <= 0 or item < 0):
            return 0
        return self.dp_matrix[weight-1][item]

    def set(self, weight, item, new_value):
        self.dp_matrix[weight-1][item] = new_value
        


def solve_backpack(backpack_weight, items):
    num_items = len(items)
    dp_matrix = DPMatrix(backpack_weight, num_items)

    for weight_considered in range(1, backpack_weight+1):
        for item_considered in range(0, num_items):
            new_item_weight, new_item_value = items[item_considered]
            options_possible = []
            # Possible value if object is included
            if weight_considered - new_item_weight >= 0:
                options_possible.append(
                    dp_matrix.get(weight_considered-new_item_weight, item_considered - 1)+ new_item_value)

            # Possible value if object is not included
            options_possible.append(dp_matrix.get(weight_considered, item_considered - 1))

            dp_matrix.set(weight_considered, item_considered, max(options_possible))
    
    backtrack_weight = backpack_weight
    backtrack_item = num_items - 1
    items_selected=[]
    while(backtrack_weight>0 and backtrack_item >= 0):
        backtrack_item_weight, backtrack_item_value = items[backtrack_item]
        backtrack_value = dp_matrix.get(backtrack_weight, backtrack_item)

        # If item weight is larger than weight available in bag
        if (backtrack_weight-backtrack_item_weight<0):
            backtrack_item-=1
            continue

        # This is the value if the item being considered was included.
        # If the current value is not this value, the item was NOT included.
        backtrack_item_incl_value = backtrack_item_value + \
            dp_matrix.get(backtrack_weight-backtrack_item_weight, backtrack_item - 1)

        if (backtrack_value == backtrack_item_incl_value):
            items_selected.append(backtrack_item)
            backtrack_weight -= backtrack_item_weight

        # Move onto next item
        backtrack_item -= 1

    return items_selected



def item_parser(line):
    return list(map(int,line.split(" ")))

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    backpack_weight = int(input_lines[0])
    items = list(map(item_parser, input_lines[1:]))
    soln = solve_backpack(backpack_weight, items)

    # print(backpack_weight)
    # print(items)
    # print(soln)
