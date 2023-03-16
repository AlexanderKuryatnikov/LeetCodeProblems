from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example': [
        [9, 3, 15, 20, 7],
        [9, 15, 7, 20, 3],
        [3,
         9, 20,
         None, None, 15, 7]
    ],
    '2: single element': [
        [-1],
        [-1],
        [-1]
    ],
    '3: complete tree': [
        [2, 1, 3],
        [2, 3, 1],
        [1, 2, 3]
    ],
    '4: right is none': [
        [2, 1],
        [2, 1],
        [1, 2]
    ],
    '5: left is none': [
        [1, 3],
        [3, 1],
        [1, None, 3]
    ],
}


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    tree_list = []
    if root is None:
        return tree_list

    def deconstruct_tree(node, i) -> None:
        if len(tree_list) < i + 1:
            tree_list.extend([None] * (i - len(tree_list) + 1))
        tree_list[i] = node.val
        if node.left is not None:
            deconstruct_tree(node=node.left, i=2 * i + 1)
        if node.right is not None:
            deconstruct_tree(node=node.right, i=2 * i + 2)

    deconstruct_tree(node=root, i=0)
    return tree_list


def test():
    for test, values in TEST_VALUES.items():
        result = solution.buildTree(values[0], values[1])
        result = tree_to_list(result)
        assert result == values[2], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
