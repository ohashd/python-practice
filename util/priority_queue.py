from operator import itemgetter

class PriorityQueue():

    class PriorityQueueItem:
        def __init__(self, item, priority):
            self.item = item
            self.priority = priority

        def __repr__(self):
            return f"({self.priority}:{self.item})"

    def __init__(self):
        self._minheap = []
        self._item_to_index_map = {}
    

    def __repr__(self):
        return self._minheap.__repr__()

    @property
    def length(self):
        return len(self._minheap)

    def _item_of(self, index):
        return self._minheap[index].item

    def _priority_of(self, index):
        return self._minheap[index].priority

    def _swap(self, index1, index2):
        temp = self._minheap[index1]
        self._minheap[index1] = self._minheap[index2]
        self._minheap[index2] = temp

        self._item_to_index_map[self._item_of(index1)] = index1
        self._item_to_index_map[self._item_of(index2)] = index2

    def _sift_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self._priority_of(index) < self._priority_of(parent_index):

                self._swap(index, parent_index)
                index = parent_index

            else:
                break

    def _sift_down(self, index):
        while index < self.length - 1:

            left_index = index*2+1
            right_index = index*2+2
            smallest_index_candidates = filter(lambda x: x < self.length, [left_index, right_index, index])

            smallest_index = min(smallest_index_candidates, key=self._priority_of)
            if (smallest_index == index):
                return
            else:
                self._swap(smallest_index, index)
                index = smallest_index
    

    def insert(self, item, priority):
        priority_queue_item = self.PriorityQueueItem(item=item, priority=priority)
        self._minheap.append(priority_queue_item)
        self._item_to_index_map[item] = self.length - 1
        self._sift_up(self.length - 1)
    
    def pop_min(self):
        ret = self._minheap[0]
        self._minheap[0] = self._minheap.pop(self.length -1)
        self._sift_down(0)
        self._item_to_index_map.pop(ret.item, None)
        return ret.item

    def change_priority(self, item, new_priority):
        index = self._item_to_index_map[item]
        old_priority = self._priority_of(index)
        self._minheap[index].priority = new_priority
        if old_priority > new_priority:
            self._sift_up(index)
        else:
            self._sift_down(index)
            