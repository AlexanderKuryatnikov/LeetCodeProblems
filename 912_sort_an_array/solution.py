from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        nums_left = self.sortArray(nums[0: len(nums) // 2])
        nums_right = self.sortArray(nums[len(nums) // 2: len(nums)])

        result = []
        left, right = 0, 0
        while left < len(nums_left) and right < len(nums_right):
            if nums_left[left] <= nums_right[right]:
                result.append(nums_left[left])
                left += 1
            else:
                result.append(nums_right[right])
                right += 1

        while left < len(nums_left):
            result.append(nums_left[left])
            left += 1
        while right < len(nums_right):
            result.append(nums_right[right])
            right += 1

        return result
