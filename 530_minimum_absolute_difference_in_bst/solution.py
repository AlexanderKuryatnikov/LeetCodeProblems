from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.sorted_array = []
        self.traverse_tree(root)
        min_val_difference = self.sorted_array[1] - self.sorted_array[0]
        for i in range(2, len(self.sorted_array)):
            min_val_difference = min(
                min_val_difference,
                self.sorted_array[i] - self.sorted_array[i - 1]
            )
        return min_val_difference

    def traverse_tree(self, node: TreeNode) -> None:
        if node.left:
            self.traverse_tree(node.left)
        self.sorted_array.append(node.val)
        if node.right:
            self.traverse_tree(node.right)
