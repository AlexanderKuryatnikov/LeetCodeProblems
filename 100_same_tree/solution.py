from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def reqursive_compare(
                node_p: Optional[TreeNode],
                node_q: Optional[TreeNode]
        ) -> bool:
            if node_p is None and node_q is None:
                return True
            if node_p is None or node_q is None:
                return False
            if node_p.val != node_q.val:
                return False
            if reqursive_compare(node_p.left, node_q.left) is False:
                return False
            if reqursive_compare(node_p.right, node_q.right) is False:
                return False
            return True

        return reqursive_compare(p, q)
