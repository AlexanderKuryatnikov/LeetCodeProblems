from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        zeroes = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                zeroes += 1
                result += zeroes
                i += 1
            else:
                zeroes = 0
                while i < len(nums) and nums[i] != 0:
                    i += 1

        return result
