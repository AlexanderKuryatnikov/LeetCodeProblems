from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes_sum = 0
        dummy = ListNode()
        new_node = dummy
        head = head.next

        while head:
            if head.val == 0:
                new_node.next = ListNode(val=nodes_sum)
                new_node = new_node.next
                nodes_sum = 0
            else:
                nodes_sum += head.val
            head = head.next

        return dummy.next
