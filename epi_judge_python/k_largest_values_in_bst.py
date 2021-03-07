from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils



def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    #inorder: numbers in increasing order

    def inorder(tree):
        return inorder(tree.left)+[tree.data]+inorder(tree.right) if tree else []

    result = inorder(tree)
    result.sort(reverse=True)
    return result[:k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
