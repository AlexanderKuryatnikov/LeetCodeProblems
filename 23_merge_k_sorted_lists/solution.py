import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(
            self,
            lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        queue = []
        unique_num = 1
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(queue, (lists[i].val, unique_num, lists[i]))
                unique_num += 1
                lists[i] = lists[i].next

        dummy = ListNode()
        current_node = dummy

        while queue:
            current_node.next = heapq.heappop(queue)[2]
            current_node = current_node.next
            if current_node.next is not None:
                heapq.heappush(
                    queue,
                    (current_node.next.val, unique_num, current_node.next)
                )
                unique_num += 1

        return dummy.next
