from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
            self,
            head: Optional[ListNode],
            k: int
    ) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        current_node = head
        i = 1
        while current_node.next is not None:
            current_node = current_node.next
            i += 1

        k = i - k % i
        if k == i:
            return head

        tail = current_node
        current_node = head

        for i in range(k - 1):
            current_node = current_node.next

        tail.next = head
        head = current_node.next
        current_node.next = None
        return head
