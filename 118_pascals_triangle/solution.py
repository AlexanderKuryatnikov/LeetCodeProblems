from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(1, numRows):
            triangle.append([])
            triangle[row].append(1)
            for i in range(1, row):
                triangle[row].append(
                    triangle[row - 1][i - 1] + triangle[row - 1][i]
                )
            triangle[row].append(1)
        return triangle
