from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: same tree': [
        [1, 2, 3],
        [1, 2, 3],
        True
    ],
    '2: different trees 1': [
        [1, 2],
        [1, None, 2],
        False
    ],
    '2: different trees 2': [
        [1, 2, 1],
        [1, 1, 2],
        False
    ],
    '3: no trees': [
        [],
        [],
        True
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
        root1 = list_to_tree(values[0])
        root2 = list_to_tree(values[1])
        result = solution.isSameTree(root1, root2)
        assert result == values[2], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
