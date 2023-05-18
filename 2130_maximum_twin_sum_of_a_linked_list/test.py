from typing import List, Optional

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: leetcode example 1': [
        [5, 4, 2, 1],
        6
    ],
    '2: leetcode example 2': [
        [4, 2, 2, 3],
        7
    ],
    '3: leetcode example 3': [
        [1, 100000],
        100001
    ],
    '4: head is none': [
        [],
        0
    ],
    '5: one element': [
        [1],
        0
    ],
    '6: three elements': [
        [1, 10, 3],
        4
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


def test():
    for test, values in TEST_VALUES.items():
        result = solution.pairSum(list_to_list_node(values[0]))
        assert values[1] == result, f'Test {test}. Your result {result}'
        print(f'Test {test}... OK')
