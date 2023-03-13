from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1,
         2, 3,
         4, 5, None, 6,
         7, None, None, None, None, None, None, 8],
        15
    ],
    '2: leetcode example 2': [
        [6,
         7, 8,
         2, 7, 1, 3,
         9, None, 1, 4, None, None, None, 5],
        19
    ],
    '3: one node': [
        [10],
        10
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
        result = solution.deepestLeavesSum(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
