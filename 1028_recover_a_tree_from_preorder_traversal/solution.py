from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        i = 0
        node_val = ''
        while i < n and traversal[i] != '-':
            node_val += traversal[i]
            i += 1

        root = TreeNode(val=int(node_val))
        node_stack = [(0, root)]

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            node_val = ''
            while i < n and traversal[i] != '-':
                node_val += traversal[i]
                i += 1

            new_node = TreeNode(val=int(node_val))

            while node_stack[-1][0] > depth - 1:
                del node_stack[-1]

            if node_stack[-1][1].left is None:
                node_stack[-1][1].left = new_node
            else:
                node_stack[-1][1].right = new_node
            node_stack.append((depth, new_node))

        return root
