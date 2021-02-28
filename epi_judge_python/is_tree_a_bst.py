from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import generate_preorder


def is_binary_tree_bst(tree: BinaryTreeNode, low=float("-inf"), high=float("inf")) -> bool:
    if tree is None:
        return True
    elif not low <= tree.data <= high:
        return False
    else:
        return is_binary_tree_bst(tree.left, low, tree.data) and \
               is_binary_tree_bst(tree.right, tree.data, high)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
