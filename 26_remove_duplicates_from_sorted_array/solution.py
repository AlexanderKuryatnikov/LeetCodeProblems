from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        unique_index = 0
        while index < len(nums):
            if nums[index] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[index]
            index += 1
        return unique_index + 1
