from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.recursive_invert(node=root)
        return root

    def recursive_invert(self, node: TreeNode):
        node.left, node.right = node.right, node.left
        if node.left is not None:
            self.recursive_invert(node=node.left)
        if node.right is not None:
            self.recursive_invert(node=node.right)
