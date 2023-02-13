from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            next_place = 0
            if digits[i] + next_place < 9:
                digits[i] += 1 + next_place
                break
            else:
                digits[i] = 0
                next_place = 1
        else:
            if next_place:
                return [1] + digits
        return digits
