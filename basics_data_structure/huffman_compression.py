"""
Huffman Tree

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/huffman_compression.html
"""

import unittest
import heapq
from collections import Counter, OrderedDict, deque
from abc import abstractmethod
from math import ceil, log2

from .binary_tree import TreeNode


class BaseCompress:

    def __init__(self, string) -> None:
        assert len(string) >= 1
        self.string = string

    @abstractmethod
    def compress(self) -> str:
        pass

    @abstractmethod
    def uncompress(self, bits) -> str:
        pass


class SimpleCompress(BaseCompress):

    def __init__(self, string) -> None:
        super().__init__(string)
        self.symbols = set(string)
        self.num_bits = ceil(log2(len(self.symbols)))
        self.char_to_bits = {}
        for idx, char in enumerate(self.symbols):
            self.char_to_bits[char] = '{:04b}'.format(idx)
        self.bits_to_char = {bits: char for char, bits in self.char_to_bits.items()}

    def compress(self) -> str:
        bits_list = map(lambda char: self.char_to_bits[char], self.string)
        return ''.join(bits_list)

    def uncompress(self, bits) -> str:
        char_list = [self.bits_to_char[bits[idx * self.num_bits:(idx + 1) * self.num_bits]]
                     for idx in range(len(bits) // 4)]
        return ''.join(char_list)


class TrieNode(TreeNode):

    def __init__(self, val, char='') -> None:
        """
        Node for trie

        :param val: occurrences of given char
        :type val: int
        :param char: character
        :type char: str
        """
        super().__init__(val)
        # character
        self.char = char
        # coding of given character
        self.coding = ''

    def __eq__(self, o) -> bool:
        return self.val == o.val

    def __ne__(self, o) -> bool:
        return self.val != o.val

    def __ge__(self, o) -> bool:
        return self.val > o.val

    def __le__(self, o) -> bool:
        return self.val < o.val

    def __gt__(self, o) -> bool:
        return self.val >= o.val

    def __lt__(self, o) -> bool:
        return self.val <= o.val


class HuffmanCompression(BaseCompress):

    def __init__(self, string) -> None:
        """
        Compressing given string by huffman coding

        :param string: given string to compress
        :type string: str
        """
        super().__init__(string)
        # string
        self.counter = Counter(string)
        # construct heap
        self.heap = []
        for char, val in self.counter.items():
            heapq.heappush(self.heap, TrieNode(val=val, char=char))
        # construct trie
        while len(self.heap) != 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            node = TrieNode(val=left.val + right.val)
            node.left, node.right = left, right
            heapq.heappush(self.heap, node)
        # construct dict
        self.root = self.heap[0]
        self.char_to_binary = self.bfs_encode(self.root)

    @staticmethod
    def bfs_encode(root):
        """
        Construct character-to-binary dictionary by breadth-first search

        :param root: root node of heap
        :type root: TrieNode
        :return: character-to-binary dictionary
        :rtype: dict
        """
        char_to_binary = OrderedDict()
        node_queue = deque([root])
        while node_queue:
            curr = node_queue.popleft()
            if curr.char != '':
                char_to_binary[curr.char] = curr.coding
                continue
            if curr.left is not None:
                curr.left.coding = curr.coding + '0'
                node_queue.append(curr.left)
            if curr.right is not None:
                curr.right.coding = curr.coding + '1'
                node_queue.append(curr.right)

        return char_to_binary

    def compress(self):
        binary_list = map(lambda char: self.char_to_binary[char], self.string)
        return ''.join(binary_list)

    def uncompress(self, bits):
        string = ''
        curr = self.root
        for bit in bits:
            if bit == '0':
                curr = curr.left
            else:
                curr = curr.right
            if curr.char != '':
                string += curr.char
                curr = self.root
        return string


class TestHuffmanCompression(unittest.TestCase):

    def test_simple_compression(self):
        string = 'hello world!'
        simple = SimpleCompress(string)
        compressed = simple.compress()
        uncompressed = simple.uncompress(compressed)
        self.assertEqual(string, uncompressed)
        print('compress rate for simple method: {:.2f}%'.format(100 * len(compressed) / (len(string) * 8)))

    def test_huffman_compression(self):
        string = 'hello world!'
        huffman = HuffmanCompression(string)
        compressed = huffman.compress()
        uncompressed = huffman.uncompress(compressed)
        self.assertEqual(string, uncompressed)
        print('compress rate for huffman method: {:.2f}%'.format(100 * len(compressed) / (len(string) * 8)))


if __name__ == '__main__':
    unittest.main()
