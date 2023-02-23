import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
            self,
            k: int,
            w: int,
            profits: List[int],
            capital: List[int]
    ) -> int:
        projects = []
        queue = []
        n = len(profits)
        for i in range(n):
            projects.append((capital[i], profits[i]))
        projects.sort()

        i = 0
        while k:
            while i < n and projects[i][0] <= w:
                heapq.heappush(queue, -projects[i][1])
                i += 1

            if not queue:
                break
            w -= heapq.heappop(queue)
            k -= 1

        return w
