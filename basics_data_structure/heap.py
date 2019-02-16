"""
Heap

- https://algorithm.yuanbin.me/zh-hans/basics_data_structure/heap.html
- https://www.geeksforgeeks.org/binary-heap/
- Algorithm 4th ed. Section 2.6 Priority Queue
"""

import unittest


class MaxHeap:

    def __init__(self, val_list=None) -> None:
        """
        Max-Heap

        In a Max-Heap the key present at the root node must be greatest
        among the keys present at all of it’s children. The same property
        must be recursively true for all sub-trees in that Binary Tree.

        :param val_list: list of node to initialize heap
        :type val_list: list
        """
        super().__init__()
        if val_list is None:
            val_list = []
        self._heap = val_list
        self._heapify()

    def _less(self, i, j):
        """
        Compare values of two given nodes

        :param i: index of the first node
        :type i: int
        :param j: index of the second node
        :type j: int
        :return: whether or not node i is less than node j
        :rtype: bool
        """
        return self._heap[i] < self._heap[j]

    def _exchange(self, i, j) -> None:
        """
        Exchange two given nodes

        :param i: index of the first node
        :type i: int
        :param j: index of the second node
        :type j: int
        """
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    @staticmethod
    def _father(idx):
        """
        Get index of father node

        :param idx: index of child node
        :type idx: int
        :return: index of father node
        :rtype: int
        """
        return (idx - 1) // 2

    @staticmethod
    def _child(idx):
        """
        Get index of children node

        :param idx: index of father node
        :type idx: int
        :return: index of children node
        :rtype: int
        """
        return 2 * idx + 1, 2 * idx + 2

    def _sink(self, idx) -> None:
        """
        Sink from top to bottom

        :param idx: index of starting node
        :type idx: int
        """
        max_idx = idx
        left_child, right_child = self._child(idx)
        if left_child < len(self) and self._less(max_idx, left_child):
            max_idx = left_child
        if right_child < len(self) and self._less(max_idx, right_child):
            max_idx = right_child
        if idx != max_idx:
            self._exchange(idx, max_idx)
            self._sink(max_idx)

    def _swim(self, idx) -> None:
        """
        Swim from bottom to top

        :param idx: index of starting node
        :type idx: int
        """
        if idx == 0:
            return
        if self._less(self._father(idx), idx):
            self._exchange(self._father(idx), idx)
            self._swim(self._father(idx))

    def _heapify(self):
        """
        Heapify given array
        """
        for idx in range(len(self) // 2, -1, -1):
            self._sink(idx)

    def push(self, node):
        """
        Push node to the heap

        :param node: node to append
        :type node: Any
        """
        self._heap.append(node)
        self._swim(len(self._heap) - 1)

    def pop(self):
        """
        Pop the root node from heap

        :return: the root node from heap
        :rtype: Any
        """
        self._exchange(0, -1)
        node = self._heap.pop()
        self._sink(0)
        return node

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        return ' '.join([str(node.val) for node in self._heap])


class MinHeap(MaxHeap):

    def _less(self, i, j):
        return not super()._less(i, j)


class TestHeap(unittest.TestCase):

    def test_max_heap(self):
        val_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        heap = MaxHeap(val_list[:])
        size = len(heap)
        # test pop
        pop_list = [heap.pop() for _ in range(size)]
        self.assertListEqual(sorted(val_list, reverse=True), pop_list)
        # test push
        for i in val_list:
            heap.push(i)
        pop_list = [heap.pop() for _ in range(size)]
        self.assertListEqual(sorted(val_list, reverse=True), pop_list)

    def test_min_heap(self):
        val_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        heap = MinHeap(val_list[:])
        size = len(heap)
        # test pop
        pop_list = [heap.pop() for _ in range(size)]
        self.assertListEqual(sorted(val_list), pop_list)
        # test push
        for i in val_list:
            heap.push(i)
        pop_list = [heap.pop() for _ in range(size)]
        self.assertListEqual(sorted(val_list), pop_list)


if __name__ == '__main__':
    unittest.main()
