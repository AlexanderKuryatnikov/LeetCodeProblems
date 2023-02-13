from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        result = [intervals[0]]
        for interval in intervals:
            if interval[0] > result[-1][1]:
                result.append(interval)
            else:
                result[-1][1] = max(interval[1], result[-1][1])
        return result
