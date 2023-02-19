from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: no tree': [
        [],
        []
    ],
    '2: depth 0': [
        [1],
        [[1]]
    ],
    '3: depth 1': [
        [1, 2, 3],
        [[1], [3, 2]]
    ],
    '4: incomplete tree': [
        [3, 9, 20, None, None, 15, 7],
        [[3], [20, 9], [15, 7]]
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


def test():
    for test, values in TEST_VALUES.items():
        root = list_to_tree(values[0])
        result = solution.zigzagLevelOrder(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
