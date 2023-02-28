from typing import List, Optional

from solution import TreeNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [1,
         2, 3,
         4, None, 2, 4,
         None, None, None, None, 4],
        [[2, 3], [3]]
    ],
    '2: leetcode example 2': [
        [2,
         1, 1],
        [[1]]
    ],
    '3: leetcode example 3': [
        [2,
         2, 2,
         3, None, 3, None],
        [[2, 3], [3]]
    ],
    '4: fake duplicates': [
        [1,
         2, 2,
         2, 5, 2, 5,
         None, None, None, None, 2, 5],
        [[2], [5]]
    ],
    '5: no subtrees': [
        [1],
        []
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
        nodes = solution.findDuplicateSubtrees(root)
        result = []
        for node in nodes:
            result.append(tree_to_list(node))
        assert result.sort() == values[1].sort(), (
            f'Test {test}. Your result {result}'
        )
        print(f'Test {test}... OK')
