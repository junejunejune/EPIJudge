from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int, currMinNode) -> Optional[BstNode]:
    # TODO - you fill in here.
    # INORDER: left->root->right
    if not tree:
        return currMinNode

    #currMinNode 업데이트
    if tree.data > k and (not currMinNode or tree.data <= currMinNode.data):
        currMinNode = tree

    if tree.data > k:
        #left에 더k와 가깝게 큰 것 있나 봐야 됨
        #만약 없으면 현재 노트가 답
        return find_first_greater_than_k(tree.left, k, currMinNode)
    else:
        #left subtree와 root는 아니므로, right subtree를 봐야함
        return find_first_greater_than_k(tree.right, k, currMinNode)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k, None)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
