from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_int = 0
        last_int = 0
        for num in arr:
            if num != last_int + 1:
                diff = num - last_int - 1
                if missing_int + diff >= k:
                    return last_int + k - missing_int
                else:
                    missing_int += diff
            last_int = num
        return num + k - missing_int
