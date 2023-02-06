from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_nums = []
        for i in range(n):
            shuffled_nums.extend((nums[i], nums[i + n]))
        return shuffled_nums
