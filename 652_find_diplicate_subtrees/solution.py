from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
            self,
            root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        subtrees = set()
        duplicates = set()
        result = []

        def find_subtrees(node):
            if node is None:
                return ''

            subtree_str = (
                str(node.val)
                + f'({find_subtrees(node.left)})'
                + f'({find_subtrees(node.right)})'
            )
            if subtree_str not in subtrees:
                subtrees.add(subtree_str)
            elif subtree_str not in duplicates:
                duplicates.add(subtree_str)
                result.append(node)

            return subtree_str

        find_subtrees(root)
        return result
