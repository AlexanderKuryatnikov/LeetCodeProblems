from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: depth 1': [
        [2, 1, 3],
        [2, 3, 1]
    ],
    '2: depth 0': [
        [1],
        [1]
    ],
    '3: no nodes': [
        [],
        []
    ],
    '4: depth 2:': [
        [4, 2, 7, 1, 3, 6, 9],
        [4, 7, 2, 9, 6, 3, 1]
    ],
    '5: incomplete tree': [
        [0, 1, 2, None, 3, 4, None, None, None, None, None, 5, 6],
        [0, 2, 1, None, 4, 3, None, None, None, 6, 5]
    ],
}


def list_to_tree(tree_list: List[int]) -> Optional[TreeNode]:
    n = len(tree_list)
    if n == 0:
        return None

    def construct_tree(i: int = 0) -> TreeNode:
        if i >= n or tree_list[i] is None:
            return None
        node = TreeNode(val=tree_list[i])
        node.left = construct_tree(2 * i + 1)
        node.right = construct_tree(2 * i + 2)
        return node

    return construct_tree()


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
        root = list_to_tree(values[0])
        result = solution.invertTree(root)
        result = tree_to_list(result)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
