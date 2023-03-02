from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        len_height = len(height)
        left = 0
        left_last = 0
        right = len_height - 1
        right_last = len_height - 1
        volume = 0

        while True:
            left += 1
            while left < len_height and height[left] < height[left_last]:
                left += 1
            if left == len_height:
                break

            current_height = height[left_last]
            while left_last < left:
                volume += current_height - height[left_last]
                left_last += 1

        while left_last < right_last:
            right -= 1
            while left_last <= right and height[right] < height[right_last]:
                right -= 1

            current_height = height[right_last]
            while right < right_last:
                volume += current_height - height[right_last]
                right_last -= 1

        return volume
