from collections import deque
from typing import List, Optional

from solution import Node, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [[0, 1],
         [1, 0]],
        [[0, 1],
         [1, 0], [1, 1], [1, 1], [1, 0]]
    ],
    '2: leetcode example 2': [
        [[1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 0, 0, 0]],
        [[0, 1],
         [1, 1], [0, 1], [1, 1], [1, 0],
         None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
    ],
    '3: 1x1': [
        [[1]],
        [[1, 1]]
    ],
}


def quad_tree_to_list(root: Node) -> List[Optional[List[int]]]:
    tree_list = []
    queue = deque([root])
    nodes_in_queue = 1
    while queue:
        if nodes_in_queue == 0:
            break

        node = queue.popleft()
        if node is None:
            tree_list.append(node)
            continue
        else:
            nodes_in_queue -= 1

        for children in (node.topLeft,
                         node.topRight,
                         node.bottomLeft,
                         node.bottomRight):
            if children is not None:
                nodes_in_queue += 1

        queue.extend([node.topLeft,
                      node.topRight,
                      node.bottomLeft,
                      node.bottomRight])
        tree_list.append([node.isLeaf, node.val])

    return tree_list


def test():
    for test, values in TEST_VALUES.items():
        result = solution.construct(values[0])
        result = quad_tree_to_list(result)
        assert result == values[1], f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
