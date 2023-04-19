from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1,
         None, 1,
         None, None, 1, 1,
         None, None, None, None, None, None, 1, 1,
         None, None, None, None, None, None, None, None, None, None, None, None, None, 1, None, None,   # noqa
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 1],   # noqa
        3
    ],
    '2: leetcode example 2': [
        [1,
         2, 3,
         None, 4, None, None,
         None, None, 5, 6, None, None, None, None,
         None, None, None, None, None, 7],
        4
    ],
    '3: one node': [
        [1],
        0
    ]
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
        result = solution.longestZigZag(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
