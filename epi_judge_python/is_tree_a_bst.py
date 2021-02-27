from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import generate_preorder


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if tree is None:
        return True

    if tree.left:
        if tree.data < tree.left.data:
            return False
        left_sub = generate_preorder(tree.left)
        if max(left_sub) > tree.data:
            return False
    if tree.right:
        if tree.data > tree.right.data:
            return False
        right_sub = generate_preorder(tree.right)
        if min(right_sub) < tree.data:
            return False

    left = is_binary_tree_bst(tree.left)
    right = is_binary_tree_bst(tree.right)

    return left and right


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
