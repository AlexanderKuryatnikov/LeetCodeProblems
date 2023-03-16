from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(
            self,
            inorder: List[int],
            postorder: List[int]
    ) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(val=postorder[0])

        root_val = postorder[-1]
        inorder_root_ind = inorder.index(root_val)

        return TreeNode(
            val=root_val,
            left=self.buildTree(
                inorder[0: inorder_root_ind],
                postorder[0: inorder_root_ind]
            ),
            right=self.buildTree(
                inorder[inorder_root_ind + 1:],
                postorder[inorder_root_ind: -1]
            )
        )
