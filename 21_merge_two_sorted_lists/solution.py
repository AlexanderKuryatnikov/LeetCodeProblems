from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next

        prev_node = head
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                prev_node.next = list2
                list2 = list2.next
            else:
                prev_node.next = list1
                list1 = list1.next
            prev_node = prev_node.next

        if list1 is None:
            prev_node.next = list2
        else:
            prev_node.next = list1

        return head
