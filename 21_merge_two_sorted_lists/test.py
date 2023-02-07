from typing import List, Optional

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: both lists empty': [
        [],
        [],
        []
    ],
    '2: first list is empty': [
        [1, 2, 3, 4],
        [],
        [1, 2, 3, 4]
    ],
    '3: second list is empty': [
        [],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ],
    '4: lists with len 1': [
        [1],
        [2],
        [1, 2]
    ],
    '5: lists need sorting': [
        [1, 3, 4, 7, 9, 10],
        [2, 5, 6, 8, 10, 11],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11]
    ],
    '6: list merged in the middle 1': [
        [1, 10],
        [2, 3, 4, 5],
        [1, 2, 3, 4, 5, 10]
    ],
    '7: list merged in the middle 2': [
        [1, 2, 7, 8],
        [3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6, 7, 8]
    ],
    '8: lists do not intersect': [
        [1, 2, 3],
        [4, 5, 6],
        [1, 2, 3, 4, 5, 6]
    ],
    '9: repeating numbers 1': [
        [1, 2, 4],
        [1, 3, 4],
        [1, 1, 2, 3, 4, 4]
    ],
    '10: repeating numbers 2': [
        [1, 2, 3],
        [2, 3, 4],
        [1, 2, 2, 3, 3, 4]
    ],
    '11: repeating numbers 3': [
        [-9, -7, -3, -3, -1, 2, 3],
        [-7, -7, -6, -6, -5, -3, 2, 4],
        [-9, -7, -7, -7, -6, -6, -5, -3, -3, -3, -1, 2, 2, 3, 4]
    ],
    '12: repeating numbers 4': [
        [-7, -7, -6, -6, -5, -3, 2, 4],
        [-9, -7, -3, -3, -1, 2, 3],
        [-9, -7, -7, -7, -6, -6, -5, -3, -3, -3, -1, 2, 2, 3, 4]
    ],
    '13: repeating numbers 5': [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ],
    '14: repeating numbers 6': [
        [-9, -5, -3, -2, -2, 3, 7],
        [-10, -8, -4, -3, -1, 3],
        [-10, -9, -8, -5, -4, -3, -3, -2, -2, -1, 3, 3, 7]
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
        head_1 = list_to_list_node(values[0])
        head_2 = list_to_list_node(values[1])
        result = solution.mergeTwoLists(head_1, head_2)
        result = list_node_to_list(result)
        assert values[2] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
