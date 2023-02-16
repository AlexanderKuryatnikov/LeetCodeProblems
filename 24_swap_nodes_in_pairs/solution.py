from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pair_first = head
        head = head.next
        while True:
            pair_second = pair_first.next
            if pair_second is None:
                break

            next_pair_first = pair_second.next
            pair_second.next = pair_first
            if next_pair_first is None or next_pair_first.next is None:
                pair_first.next = next_pair_first
                break

            pair_first.next = next_pair_first.next
            pair_first = next_pair_first

        return head
