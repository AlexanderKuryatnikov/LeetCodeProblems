from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left < right:
            middle = (left + right + 1) // 2
            if target >= matrix[middle][0]:
                left = middle
            else:
                right = middle - 1

        row = left
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True

        return False
