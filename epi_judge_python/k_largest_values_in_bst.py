from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:

    def helper(tree: BstNode):
        if tree and len(k_largest) < k:
            helper(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data)
                helper(tree.left)

    k_largest = []
    helper(tree)
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
