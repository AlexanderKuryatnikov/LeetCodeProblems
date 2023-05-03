from typing import List


class Solution:
    def findDifference(
            self,
            nums1: List[int],
            nums2: List[int]
    ) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = [[], []]

        for element in set1:
            if element not in set2:
                result[0].append(element)

        for element in set2:
            if element not in set1:
                result[1].append(element)

        return result
