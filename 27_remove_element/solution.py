from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            try:
                while nums[right] == val:
                    right -= 1
            except IndexError:
                break

            if nums[left] != val:
                left += 1
                continue

            nums[left] = nums[right]
            right -= 1
        return left
