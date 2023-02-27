from typing import List


class Node:
    def __init__(
            self,
            val,
            isLeaf,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:

        def construct_branch(
                row: int,
                col: int,
                length: int
        ):
            if length == 1:
                return grid[row][col]

            top_left = construct_branch(
                row=row,
                col=col,
                length=length // 2
            )
            top_right = construct_branch(
                row=row,
                col=col + length // 2,
                length=length // 2
            )
            bottom_left = construct_branch(
                row=row + length // 2,
                col=col,
                length=length // 2
            )
            bottom_right = construct_branch(
                row=row + length // 2,
                col=col + length // 2,
                length=length // 2
            )

            if top_left == top_right == bottom_left == bottom_right:
                return top_left

            if type(top_left) is int:
                top_left = Node(
                    isLeaf=1,
                    val=top_left,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )
            if type(top_right) is int:
                top_right = Node(
                    isLeaf=1,
                    val=top_right,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )
            if type(bottom_left) is int:
                bottom_left = Node(
                    isLeaf=1,
                    val=bottom_left,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )
            if type(bottom_right) is int:
                bottom_right = Node(
                    isLeaf=1,
                    val=bottom_right,
                    topLeft=None,
                    topRight=None,
                    bottomLeft=None,
                    bottomRight=None
                )

            return Node(
                isLeaf=0,
                val=1,
                topLeft=top_left,
                topRight=top_right,
                bottomLeft=bottom_left,
                bottomRight=bottom_right
            )

        root = construct_branch(row=0, col=0, length=len(grid))
        if type(root) is int:
            root = Node(
                isLeaf=1,
                val=root,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None
            )
        return root
