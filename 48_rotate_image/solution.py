from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range((len(matrix) + 1) // 2):
            for j in range(len(matrix) // 2):
                (
                    matrix[i][j], matrix[j][-i-1],
                    matrix[-i-1][-j-1], matrix[-j-1][i]
                ) = (
                    matrix[-j-1][i], matrix[i][j],
                    matrix[j][-i-1], matrix[-i-1][-j-1]
                )
