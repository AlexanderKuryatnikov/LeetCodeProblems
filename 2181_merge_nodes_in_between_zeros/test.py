from typing import List, Optional

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [0, 3, 1, 0, 4, 5, 2, 0],
        [4, 11]
    ],
    '2: leetcode example 2': [
        [0, 1, 0, 3, 0, 2, 2, 0],
        [1, 3, 4]
    ],
    '3: one interval': [
        [0, 5, 6, 7, 0],
        [18]
    ],
}


def list_to_list_node(regular_list: List[int]) -> Optional[ListNode]:
    if len(regular_list) == 0:
        return None

    head = ListNode(val=regular_list[0])
    if len(regular_list) == 1:
        return head

    prev_node = head
    for number in regular_list[1:]:
        current_node = ListNode(val=number)
        prev_node.next = current_node
        prev_node = current_node

    return head


def list_node_to_list(list_node: Optional[ListNode]) -> List[int]:
    if list_node is None:
        return []
    regular_list = []
    while list_node.next is not None:
        regular_list.append(list_node.val)
        list_node = list_node.next
    regular_list.append(list_node.val)
    return regular_list


def test():
    for test, values in TEST_VALUES.items():
        head = list_to_list_node(values[0])
        result = solution.mergeNodes(head)
        result = list_node_to_list(result)
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
