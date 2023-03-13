from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepest_sum = 0
        max_depth = 0

        def traverse(node: TreeNode, depth: int) -> None:
            if node.left is None and node.right is None:
                nonlocal deepest_sum, max_depth
                if depth == max_depth:
                    deepest_sum += node.val
                elif depth > max_depth:
                    max_depth = depth
                    deepest_sum = node.val
                return
            if node.left is not None:
                traverse(node.left, depth + 1)
            if node.right is not None:
                traverse(node.right, depth + 1)

        traverse(root, 0)

        return deepest_sum
