from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: same depth': [
        [1, 2, 3],
        25
    ],
    '2: different depth': [
        [4, 9, 0, 5, 1],
        1026
    ],
    '3: single node': [
        [4],
        4
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
        result = solution.sumNumbers(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
