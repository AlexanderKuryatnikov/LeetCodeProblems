from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        numbers = deque([])
        max_twin_sum = 0

        if head is None:
            return max_twin_sum
        while head:
            numbers.append(head.val)
            head = head.next

        while len(numbers) > 1:
            twin_sum = numbers.popleft() + numbers.pop()
            if max_twin_sum < twin_sum:
                max_twin_sum = twin_sum

        return max_twin_sum
