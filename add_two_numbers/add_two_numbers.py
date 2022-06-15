# Given two linked lists, each representing a single integer
# in reverse order, find the sum of the two numbers and
# return it in a similar linked list. e.g.
#
# 2 4 3
# 5 6 4
#
# returns 7 0 8
# (342 + 465 = 807)
from __future__ import annotations
import sys
from typing import Optional

class Node():
    def __init__(self, val: int, next: Optional[Node]=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def from_list(val_list):
        last_node = None
        for val in reversed(val_list):
            last_node = Node(val, last_node)
        return last_node
    
    def copy(self):
        if self.next == None:
            return Node(self.val, None)
        else:
            return Node(self.val, self.next.copy())

    def __repr__(self):
        if self.next == None:
            return f"{self.val}"
        else:
            return f"{self.val} {self.next.__repr__()}"

def add_two_numbers(num_1: Node, num_2: Node):
    def _add_two_numbers(num_1: Optional[Node], num_2: Optional[Node], carryover: int):

        if num_1 == None and num_2 == None:
            return None
        
        if num_1 == None:
            return num_2.copy()
        
        if num_2 == None:
            return num_1.copy()

        digit_sum = num_1.val + num_2.val + carryover
        carryover = 0

        if digit_sum >= 10:
            carryover = 1
            digit_sum -= 10

        return Node(digit_sum, _add_two_numbers(num_1.next, num_2.next, carryover))
    
    return _add_two_numbers(num_1, num_2, 0)
        

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    num_1 = list(map(int, input_lines[0].split(" ")))
    num_2 = list(map(int, input_lines[1].split(" ")))

    num_1_ll = Node.from_list(num_1)
    num_2_ll = Node.from_list(num_2)  

    print(num_1_ll)
    print(num_2_ll)     

    print(add_two_numbers(num_1_ll, num_2_ll))
