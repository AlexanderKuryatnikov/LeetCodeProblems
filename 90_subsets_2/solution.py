from collections import defaultdict
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        for num in nums_dict:
            new_subsets = []

            while nums_dict[num] > 0:
                for subset in subsets:
                    new_subsets.append(subset + [num] * nums_dict[num])
                nums_dict[num] -= 1

            subsets.extend(new_subsets)

        return subsets
