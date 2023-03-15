from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: complete tree': [
        [1,
         2, 3,
         4, 5, 6],
        True
    ],
    '2: node is not as far left as possible': [
        [1,
         2, 3,
         4, 5, None, 7],
        False
    ],
    '3: not every level is filled': [
        [1,
         2, None,
         3, 4],
        False
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
        result = solution.isCompleteTree(root)
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
