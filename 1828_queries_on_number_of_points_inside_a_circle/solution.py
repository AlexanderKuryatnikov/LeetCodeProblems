from typing import List


class Solution:
    def countPoints(
            self,
            points: List[List[int]],
            queries: List[List[int]]
    ) -> List[int]:
        result = []
        for query in queries:
            circle_x, circle_y, radius = query
            points_inside = 0
            for point in points:
                point_x, point_y = point
                if (
                    (point_x - circle_x) ** 2
                    + (point_y - circle_y) ** 2
                    <= radius ** 2
                ):
                    points_inside += 1
            result.append(points_inside)
        return result
