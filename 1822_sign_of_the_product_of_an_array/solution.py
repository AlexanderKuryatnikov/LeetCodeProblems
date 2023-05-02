from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign_positive = True

        for num in nums:
            if num < 0:
                sign_positive = not sign_positive
                continue
            if num == 0:
                return 0

        if sign_positive:
            return 1
        return -1
