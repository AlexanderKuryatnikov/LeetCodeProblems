from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf_sum = 0

        def traverse(node: TreeNode, number: int) -> None:
            number = number * 10 + node.val
            if node.left is None and node.right is None:
                nonlocal root_to_leaf_sum
                root_to_leaf_sum += number
                return
            if node.left is not None:
                traverse(node.left, number)
            if node.right is not None:
                traverse(node.right, number)

        traverse(root, 0)
        return root_to_leaf_sum
