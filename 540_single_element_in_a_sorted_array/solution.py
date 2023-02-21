from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[1]:
            return nums[0]
        if nums[-2] < nums[-1]:
            return nums[-1]

        left = 1
        right = len(nums) - 2
        while left <= right:
            middle = (left + right) // 2

            if nums[middle - 1] < nums[middle] < nums[middle + 1]:
                return nums[middle]
            elif middle % 2 == 0:
                if nums[middle] == nums[middle + 1]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] == nums[middle + 1]:
                    right = middle - 1
                else:
                    left = middle + 1
