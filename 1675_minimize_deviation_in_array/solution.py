import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        queue = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] *= 2
            heapq.heappush(queue, -nums[i])

        min_num = min(nums)
        max_num = -heapq.heappop(queue)
        min_dev = max_num - min_num
        while max_num % 2 == 0:
            max_num //= 2
            if max_num < min_num:
                min_num = max_num

            heapq.heappush(queue, -max_num)
            max_num = -heapq.heappop(queue)

            if min_dev > max_num - min_num:
                min_dev = max_num - min_num

        return min_dev
