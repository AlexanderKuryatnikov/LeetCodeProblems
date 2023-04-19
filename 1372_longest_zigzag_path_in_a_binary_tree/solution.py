from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        longest = [0]

        def traverse(prev_left: bool, node: TreeNode) -> int:
            if node is None:
                return -1

            if prev_left:
                longest_sub = 1 + traverse(prev_left=True, node=node.left)
                if longest[0] < longest_sub:
                    longest[0] = longest_sub
                return 1 + traverse(prev_left=False, node=node.right)
            else:
                longest_sub = 1 + traverse(prev_left=False, node=node.right)
                if longest[0] < longest_sub:
                    longest[0] = longest_sub
                return 1 + traverse(prev_left=True, node=node.left)

        starts_from_root = max(
            1 + traverse(prev_left=True, node=root.left),
            1 + traverse(prev_left=False, node=root.right)
        )
        return max(starts_from_root, longest[0])
