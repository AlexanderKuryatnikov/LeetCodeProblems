class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        next_place_value = 0
        sum_l = l1

        while l1.next is not None and l2.next is not None:
            value = (l1.val + l2.val + next_place_value) % 10
            next_place_value = (l1.val + l2.val + next_place_value) // 10
            l1.val = value

            l1 = l1.next
            l2 = l2.next

        value = (l1.val + l2.val + next_place_value) % 10
        next_place_value = (l1.val + l2.val + next_place_value) // 10
        l1.val = value

        while l1.next is not None:
            l1 = l1.next

            value = (l1.val + next_place_value) % 10
            next_place_value = (l1.val + next_place_value) // 10
            l1.val = value

        while l2.next is not None:
            l2 = l2.next

            value = (l2.val + next_place_value) % 10
            next_place_value = (l2.val + next_place_value) // 10
            l1.next = ListNode(val=value)

            l1 = l1.next

        if next_place_value > 0:
            l1.next = ListNode(val=next_place_value)

        return sum_l


solution = Solution()
