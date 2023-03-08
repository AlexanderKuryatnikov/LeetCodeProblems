from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if sum([-(pile // -mid) for pile in piles]) <= h:
                right = mid
            else:
                left = mid + 1
        return right
