from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0, 0)])
        widest = 0

        current_lvl = 0
        first_position, last_position = 0, 0
        while queue:
            node, lvl, position = queue.popleft()
            if lvl == current_lvl:
                last_position = position
            else:
                width = last_position - first_position + 1
                if widest < width:
                    widest = width
                current_lvl = lvl
                first_position = position

            if node.left:
                queue.append((node.left, lvl + 1, position * 2 + 1))
            if node.right:
                queue.append((node.right, lvl + 1, position * 2 + 2))

        width = last_position - first_position + 1
        if widest < width:
            widest = width
        return widest
