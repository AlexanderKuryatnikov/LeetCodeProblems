from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0

        n = len(satisfaction)
        for i in range(n):
            if satisfaction[i] >= 0:
                first_positive = i
                break

        like_time = 0
        included_sum = 0
        for i in range(first_positive, n):
            included_sum += satisfaction[i]
            like_time += satisfaction[i] * (i + 1 - first_positive)

        for i in range(first_positive - 1, -1, -1):
            if satisfaction[i] + included_sum > 0:
                included_sum += satisfaction[i]
                like_time += included_sum
            else:
                break

        return like_time
