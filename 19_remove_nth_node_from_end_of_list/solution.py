from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self,
            head: Optional[ListNode],
            n: int
    ) -> Optional[ListNode]:
        current_node = head
        list_node_len = 0
        while current_node:
            list_node_len += 1
            current_node = current_node.next

        if list_node_len == n:
            return head.next

        current_node = head
        for i in range(list_node_len - n - 1):
            current_node = current_node.next
        if n == 1:
            current_node.next = None
            return head
        current_node.next = current_node.next.next
        return head
