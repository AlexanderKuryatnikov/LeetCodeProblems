from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle) - 1
        if n == 0:
            return triangle[0][0]

        for i in range(1, len(triangle) - 1):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i][-1] += triangle[i-1][-1]

        min_route = min(
            triangle[-1][0] + triangle[-2][0],
            triangle[-1][-1] + triangle[-2][-1]
        )
        for j in range(1, len(triangle[-1]) - 1):
            triangle[-1][j] += min(triangle[-2][j-1], triangle[-2][j])
            if triangle[-1][j] < min_route:
                min_route = triangle[-1][j]

        return min_route
