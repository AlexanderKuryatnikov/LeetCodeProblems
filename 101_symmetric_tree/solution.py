from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left = deque([root.left])
        right = deque([root.right])

        while left and right:
            left_node = left.popleft()
            right_node = right.popleft()

            if left_node is None and right_node is None:
                continue
            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            left.extend([left_node.left, left_node.right])
            right.extend([right_node.right, right_node.left])

        return True
