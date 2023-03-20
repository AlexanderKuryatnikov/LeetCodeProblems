from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeroes = 0
        max_allowed = 0

        i = 0
        if flowerbed[i] == 0:
            zeroes += 1

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                zeroes += 1
            elif zeroes > 0:
                max_allowed += (zeroes - 1) // 2
                zeroes = 0
            i += 1

        max_allowed += zeroes // 2

        return max_allowed >= n
