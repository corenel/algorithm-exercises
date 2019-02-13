"""
Binary Tree

https://algorithm.yuanbin.me/zh-hans/basics_data_structure/binary_tree.html
"""

import unittest


class TreeNode:

    def __init__(self, val) -> None:
        """
        Node for bianry tree

        :param val: value
        :type val: Any
        """
        self.val = val
        self.left, self.right = None, None

    def add_child(self, child):
        if self.left is None:
            self.left = child
        elif self.right is None:
            self.right = child
        else:
            raise RuntimeError('Node can only have two children')

    def get_children(self):
        """
        Return existed children

        :return: existed children
        :rtype: list[TreeNode]
        """
        children = [child for child in (self.left, self.right)
                    if child is not None]
        return children


class BinaryTree:

    def __init__(self, root=None) -> None:
        super().__init__()
        self.root = root


def depth_first_traverse_preorder(root):
    """
    Traverse a binary tree in preorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.append(root)
        node_list.extend(depth_first_traverse_preorder(root.left))
        node_list.extend(depth_first_traverse_preorder(root.right))

    return node_list


def depth_first_traverse_inorder(root):
    """
    Traverse a binary tree in inorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.extend(depth_first_traverse_inorder(root.left))
        node_list.append(root)
        node_list.extend(depth_first_traverse_inorder(root.right))

    return node_list


def depth_first_traverse_postorder(root):
    """
    Traverse a binary tree in postorder

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    if root is not None:
        node_list.extend(depth_first_traverse_postorder(root.left))
        node_list.extend(depth_first_traverse_postorder(root.right))
        node_list.append(root)

    return node_list


def broadth_first_traverse(root):
    """
    Broadth-first traversal

    :param root: root node of the binary tree
    :type root: TreeNode
    :return: traversed list
    :rtype: list[TreeNode]
    """
    node_list = []
    node_stack = [root]
    while node_stack:
        curr = node_stack.pop(0)
        node_list.append(curr)
        for child in curr.get_children():
            node_stack.append(child)

    return node_list


def generate_test_binary_tree():
    """
    Generate a binary tree for test case

    :return: root node of generated binary tree
    :rtype: TreeNode
    """
    root = TreeNode(0)
    root.add_child(TreeNode(1))
    root.add_child(TreeNode(2))
    root.left.add_child(TreeNode(3))
    root.left.add_child(TreeNode(4))
    root.right.add_child(TreeNode(5))
    root.right.add_child(TreeNode(6))

    return root


class TestBinaryTree(unittest.TestCase):

    def test_depth_first_traversal_preorder(self):
        root = generate_test_binary_tree()
        val_list = [node.val for node in depth_first_traverse_preorder(root)]
        self.assertListEqual([0, 1, 3, 4, 2, 5, 6], val_list)

    def test_depth_first_traversal_inorder(self):
        root = generate_test_binary_tree()
        val_list = [node.val for node in depth_first_traverse_inorder(root)]
        self.assertListEqual([3, 1, 4, 0, 5, 2, 6], val_list)

    def test_depth_first_traversal_postorder(self):
        root = generate_test_binary_tree()
        val_list = [node.val for node in depth_first_traverse_postorder(root)]
        self.assertListEqual([3, 4, 1, 5, 6, 2, 0], val_list)

    def test_broadth_first_traversal(self):
        root = generate_test_binary_tree()
        val_list = [node.val for node in broadth_first_traverse(root)]
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6], val_list)
