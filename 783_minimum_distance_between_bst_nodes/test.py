from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [4, 2, 6, 1, 3],
        1
    ],
    '2: leetcode example 2': [
        [1, 0, 48, None, None, 12, 49],
        1
    ],
    '3: distant nodes are closest': [
        [50, 40, 60, 30, 48],
        2
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
        result = solution.minDiffInBST(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
