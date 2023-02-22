from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        while min_cap < max_cap:
            mid_cap = (min_cap + max_cap) // 2

            shipment = 0
            days_with_mid_cap = 1
            for weight in weights:
                if shipment + weight <= mid_cap:
                    shipment += weight
                else:
                    shipment = weight
                    days_with_mid_cap += 1

            if days_with_mid_cap > days:
                min_cap = mid_cap + 1
            else:
                max_cap = mid_cap
        return min_cap
