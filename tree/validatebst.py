"""
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

"""
Tree inorder traversal to check if the values are inorder.
If so the tree is valid.
"""
def isValidBST(self, root: TreeNode) -> bool:
    stack = list()
    prev = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if prev and prev.val >= root.val:
            return False
        prev = root
        root = root.right
    return True