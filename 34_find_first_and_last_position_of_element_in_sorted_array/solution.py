from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        if right < 0:
            return [-1, -1]

        while left < right:
            middle = (left + right) // 2
            if target <= nums[middle]:
                right = middle
            else:
                left = middle + 1

        if nums[left] != target:
            return [-1, -1]
        first = left
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle
            else:
                left = middle + 1

        return [first, right - 1]
