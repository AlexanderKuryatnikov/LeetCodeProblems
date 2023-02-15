from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_str = ''
        for digit in num:
            num_str += str(digit)
        num = [int(i) for i in str(int(num_str) + k)]
        return num
