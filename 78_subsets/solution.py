from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for number in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [number])
            subsets.extend(new_subsets)
        return subsets
