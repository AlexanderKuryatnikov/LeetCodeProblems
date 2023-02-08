from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        current_spot = 0
        best_spot = 0
        jumps = 1

        while current_spot + nums[current_spot] < len(nums) - 1:

            for next_spot in range(current_spot + nums[current_spot],
                                   current_spot,
                                   -1):
                if best_spot + nums[best_spot] < next_spot + nums[next_spot]:
                    best_spot = next_spot

            current_spot = best_spot
            jumps += 1

        return jumps
