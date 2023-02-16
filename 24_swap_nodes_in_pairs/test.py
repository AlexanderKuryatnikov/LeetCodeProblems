from typing import List, Optional

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: empty list': [
        [],
        []
    ],
    '1: 1 element': [
        [1],
        [1]
    ],
    '2: 2 elements': [
        [1, 2],
        [2, 1]
    ],
    '3: 3 elements': [
        [1, 2, 3],
        [2, 1, 3]
    ],
    '4: even length': [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [2, 1, 4, 3, 6, 5, 8, 7]
    ],
    '5: odd length': [
        [1, 2, 3, 4, 5, 6, 7],
        [2, 1, 4, 3, 6, 5, 7]
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
        result = solution.swapPairs(head)
        result = list_node_to_list(result)
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
