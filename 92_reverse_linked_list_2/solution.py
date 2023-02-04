from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
                self,
                head: Optional[ListNode],
                left: int,
                right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        i = 1
        current_node = head
        while i < left - 1:
            i += 1
            current_node = current_node.next

        if left == 1:
            node_before_reverse = None
            head_reverse = current_node
        else:
            node_before_reverse = current_node
            current_node = current_node.next
            i += 1
            head_reverse = current_node

        prev_node = current_node
        current_node = current_node.next
        i += 1

        while i < right:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            i += 1

        head_reverse.next = current_node.next
        current_node.next = prev_node
        if node_before_reverse is None:
            head = current_node
        else:
            node_before_reverse.next = current_node

        return head
