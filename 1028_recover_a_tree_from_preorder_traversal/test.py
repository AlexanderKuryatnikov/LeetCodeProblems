from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        '1-2--3--4-5--6--7',
        [1,
         2, 5,
         3, 4, 6, 7]
    ],
    '2: leetcode example 2': [
        '1-2--3---4-5--6---7',
        [1,
         2, 5,
         3, None, 6, None,
         4, None, None, None, 7]
    ],
    '3: leetcode example 3': [
        '1-401--349---90--88',
        [1,
         401, None,
         349, 88, None, None,
         90]
    ],
    '4: single node': [
        '1',
        [1]
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
        result = solution.recoverFromPreorder(values[0])
        result = tree_to_list(result)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
