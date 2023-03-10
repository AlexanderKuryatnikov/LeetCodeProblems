from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        while left < right:
            mid = (left + right) // 2
            if sum([mid // bus for bus in time]) >= totalTrips:
                right = mid
            else:
                left = mid + 1
        return right
