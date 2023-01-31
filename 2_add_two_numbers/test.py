from typing import List

from solution import ListNode, Solution

solution = Solution()


TEST_VALUES = {
    '1: numbers with equal length': [
        [2, 4, 3],
        [5, 6, 4],
        [7, 0, 8]
    ],
    '2: two zeros': [
        [0],
        [0],
        [0]
    ],
    '3: first zero': [
        [0],
        [1, 2, 3],
        [1, 2, 3]
    ],
    '4: second zero': [
        [1, 2, 3],
        [0],
        [1, 2, 3]
    ],
    '5: extra digit, first number bigger': [
        [9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9],
        [8, 9, 9, 9, 0, 0, 0, 1]
    ],
    '6: extra digit, second number bigger': [
        [9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9],
        [8, 9, 9, 9, 0, 0, 0, 1]
    ],
    '7: extra digit, equal length': [
        [9, 9, 9],
        [9, 9, 9],
        [8, 9, 9, 1]
    ],
}


def input(number_list: List[int]) -> ListNode:
    first_node = ListNode(val=number_list[0])
    if len(number_list) == 1:
        return first_node

    prev_node = first_node
    for number in number_list[1:]:
        current_node = ListNode(val=number)
        prev_node.next = current_node
        prev_node = current_node

    return first_node


def output(list_node: ListNode) -> List[int]:
    number_list = []
    while list_node.next is not None:
        number_list.append(list_node.val)
        list_node = list_node.next
    number_list.append(list_node.val)
    return number_list


def test():
    for test, values in TEST_VALUES.items():
        l1 = input(values[0])
        l2 = input(values[1])
        l_sum = output(solution.addTwoNumbers(l1=l1, l2=l2))
        assert l_sum == values[2], f'Test {test}. Your result {l_sum}'
        print(f'Test {test}... OK')
