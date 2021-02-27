from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



#def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.

def is_binary_tree_bst(tree, r=[float('-inf'), float('inf')]):
    if not tree:
        return True
    if not r[0] <= tree.data <= r[1]:
        return False

    return is_binary_tree_bst(tree.left, [r[0], tree.data]) and is_binary_tree_bst(tree.right, [tree.data, r[1]])


    #return is_binary_tree_bst(tree.right) and is_binary_tree_bst(tree.left)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
