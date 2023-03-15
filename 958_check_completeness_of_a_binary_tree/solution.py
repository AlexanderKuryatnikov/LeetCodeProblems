from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        none_met = False
        while queue:
            node = queue.popleft()
            if node is None:
                none_met = True
                continue
            if none_met:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
