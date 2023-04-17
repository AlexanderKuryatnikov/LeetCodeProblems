from typing import List


class Solution:
    def kidsWithCandies(
            self,
            candies: List[int],
            extraCandies: int
    ) -> List[bool]:
        max_candies = 0
        for candy in candies:
            if max_candies < candy:
                max_candies = candy

        return [candy + extraCandies >= max_candies for candy in candies]
