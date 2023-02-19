from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        zigzag = [[]]
        queue = deque([(root, 0)])
        current_depth = 0

        while queue:
            node, depth = queue.popleft()

            if depth > current_depth:
                current_depth = depth
                zigzag.append([])
            zigzag[-1].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        for i in range(1, len(zigzag), 2):
            zigzag[i].reverse()

        return zigzag
