"""
Linked List

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/linked_list.html
"""

import unittest


class ListNode:

    def __init__(self, val) -> None:
        """
        Node for singly linked list

        :param val: value of this node
        :type val: Any
        """
        self.val = val
        self.next = None


class DListNode:
    def __init__(self, val) -> None:
        """
        Node of doubly linked list

        :param val: value of this node
        :type val: Any
        """
        self.val = val
        self.next = None
        self.prev = None


class LinkedList:

    def __init__(self, singly=True, head=None) -> None:
        """
        Linked list

        :param singly: whether or not this linked list is singly
        :type singly: bool
        :param head: head node
        :type head: ListNode or DListNode
        """
        super().__init__()
        self.singly = singly if head is None else isinstance(head, ListNode)
        self.dummy_head = self.generate_node(None)
        self.curr_node = self.dummy_head
        if head is not None:
            self.append(head)

    def generate_node(self, val):
        """
        Create node with given value

        :param val: given value
        :type val: Any
        :return: node
        :rtype: ListNode or DListNone
        """
        return ListNode(val) if self.singly else DListNode(val)

    def to_list(self):
        """
        Return list of node values

        :return: list of node values
        :rtype: list
        """
        return [node.val for node in self.traverse()]

    def get_head(self):
        """
        Get head node of linked list

        :return: head node
        :rtype: ListNode or DListNone
        """
        head = self.dummy_head.next
        assert head is not None
        return head

    def eliminate_circularity(self):
        """
        Remove circularity of linked list
        """
        curr = self.dummy_head.next
        while curr is not None:
            if curr.next == self.dummy_head.next:
                curr.next = None
                break
            curr = curr.next

    def append(self, node):
        # initialize dummy head node
        if self.dummy_head.next is None:
            self.dummy_head.next = node
        # set next pointer for current node
        self.curr_node.next = node
        # set prev pointer for new node
        if not self.singly and self.curr_node is not self.dummy_head:
            node.prev = self.curr_node
        # switch current node to the new one
        self.curr_node = node

    def append_val(self, val):
        """
        Append node with given value

        :param val: given value
        :type val: Any
        """
        self.append(self.generate_node(val))

    def append_val_list(self, val_list):
        """
        Append nodes with given value list

        :param val_list: value list
        :type val_list: list
        """
        for val in val_list:
            self.append(self.generate_node(val))

    def pop(self, index):
        """
        Pop item by index

        :param index: index of node to pop
        :type index: int
        """
        assert index >= 0
        if self.singly:
            remove_list_node(curr=self.at(index), prev=self.at(index - 1))
        else:
            remove_list_node(curr=self.at(index), prev=None if index != 0 else self.dummy_head)
        self.eliminate_circularity()

    def reverse(self):
        """
        Reverse linked list

        :return: head node of reversed linked list
        :rtype: ListNode or DListNone
        """
        head = self.get_head()

        if self.singly:
            prev = None
            while head is not None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            self.dummy_head.next = prev
            self.eliminate_circularity()
            return self.get_head()
        else:
            curr = None
            while head is not None:
                curr = head
                head = curr.next
                curr.next = curr.prev
                curr.prev = head
            self.dummy_head.next = curr
            self.eliminate_circularity()
            return self.get_head()

    def traverse(self):
        """
        Traverse linked list

        :return: list of nodes
        :rtype: list
        """
        node_list = []
        head = self.get_head()
        curr = head
        while curr is not None:
            node_list.append(curr)
            curr = curr.next
        return node_list

    def at(self, index):
        """
        Get node by index

        :param index: index of node
        :type index: int
        :return: desired node
        :rtype: ListNode or DListNone
        """
        if index < 0:
            return self.dummy_head

        head = self.get_head()
        curr = head
        cnt = 0
        while curr is not None:
            if cnt == index:
                return curr
            curr = curr.next
            cnt += 1

        raise IndexError


def remove_list_node(curr, prev=None):
    if isinstance(curr, DListNode):
        if prev is None and curr.prev is not None:
            prev = curr.prev
        if prev is not None:
            prev.next = curr.next
            del curr
    elif isinstance(curr, ListNode) and prev is not None:
        prev.next = curr.next
        del curr
    else:
        raise RuntimeError('Invalid operation to delete node')


class TestLinkedList(unittest.TestCase):

    def test_singly_linked_list(self):
        val_list = [1, 2, 3, 4, 5]
        node_list = LinkedList(singly=True)
        # test appending
        node_list.append_val_list(val_list)
        self.assertListEqual(val_list, node_list.to_list())
        # test reversing
        val_list_reversed = val_list[::-1]
        node_list_reversed = LinkedList(singly=node_list.singly, head=node_list.reverse())
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing node
        val_list_reversed.pop(2)
        node_list_reversed.pop(2)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing head node
        val_list_reversed.pop(0)
        node_list_reversed.pop(0)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing tail node
        node_list_reversed.pop(len(val_list_reversed) - 1)
        val_list_reversed.pop(-1)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        self.assertEqual(None, node_list_reversed.traverse()[-1].next)

    def test_doubly_linked_list(self):
        val_list = [1, 2, 3, 4, 5]
        node_list = LinkedList(singly=False)
        # test appending
        node_list.append_val_list(val_list)
        self.assertListEqual(val_list, node_list.to_list())
        # test reversing
        val_list_reversed = val_list[::-1]
        node_list_reversed = LinkedList(singly=node_list.singly, head=node_list.reverse())
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing node
        val_list_reversed.pop(2)
        node_list_reversed.pop(2)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing head node
        val_list_reversed.pop(0)
        node_list_reversed.pop(0)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        # test removing tail node
        node_list_reversed.pop(len(val_list_reversed) - 1)
        val_list_reversed.pop(-1)
        self.assertListEqual(val_list_reversed, node_list_reversed.to_list())
        self.assertEqual(None, node_list_reversed.traverse()[-1].next)


if __name__ == '__main__':
    unittest.main()
