from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: symmetric tree': [
        [1,
         2, 2,
         3, 4, 4, 3],
        True
    ],
    '2: asymmetric tree': [
        [1,
         2, 2,
         None, 3, None, 3],
        False
    ],
    '3: single node': [
        [1],
        True
    ],
    '4: one of children nodes is None': [
        [1,
         None, 2],
        False
    ],
    '5: asymmetric tree with diff values': [
        [1,
         2, 2,
         3, 4, 3, 4],
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
        result = solution.isSymmetric(root)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
