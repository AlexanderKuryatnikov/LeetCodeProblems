import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest1 = heapq.heappop(stones)
            largest2 = heapq.heappop(stones)
            if largest1 != largest2:
                heapq.heappush(stones, largest1 - largest2)

        if stones:
            return -stones[0]
        return 0
