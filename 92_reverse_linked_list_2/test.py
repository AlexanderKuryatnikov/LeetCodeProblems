from typing import List

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: subsequence in the middle': [
        [1, 2, 3, 4, 5, 6, 7],
        2,
        6,
        [1, 6, 5, 4, 3, 2, 7]
    ],
    '2: list length is one': [
        [10],
        1,
        1,
        [10]
    ],
    '3: list begins with subsequence': [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        1,
        5,
        [5, 4, 3, 2, 1, 6, 7, 8, 9]
    ],
    '4: list ends with subsequance': [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        6,
        9,
        [1, 2, 3, 4, 5, 9, 8, 7, 6]
    ],
    '5: subsequance with len 2': [
        [1, 2, 3, 4, 5],
        2,
        3,
        [1, 3, 2, 4, 5],
    ],
    '6: reverse whole list': [
        [1, 2, 3, 4, 5],
        1,
        5,
        [5, 4, 3, 2, 1]
    ],
}


def list_to_list_node(regular_list: List[int]) -> ListNode:
    head = ListNode(val=regular_list[0])
    if len(regular_list) == 1:
        return head

    prev_node = head
    for number in regular_list[1:]:
        current_node = ListNode(val=number)
        prev_node.next = current_node
        prev_node = current_node

    return head


def list_node_to_list(list_node: ListNode) -> List[int]:
    regular_list = []
    while list_node.next is not None:
        regular_list.append(list_node.val)
        list_node = list_node.next
    regular_list.append(list_node.val)
    return regular_list


def test():
    for test, values in TEST_VALUES.items():
        head = list_to_list_node(values[0])
        result = solution.reverseBetween(head, values[1], values[2])
        result = list_node_to_list(result)
        assert values[3] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
