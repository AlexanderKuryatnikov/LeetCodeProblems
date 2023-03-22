from collections import defaultdict, deque
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        roads_dict = defaultdict(list)
        for road in roads:
            roads_dict[road[0]].append((road[1], road[2]))
            roads_dict[road[1]].append((road[0], road[2]))

        visited_cities = {1}
        visited_roads = set()
        queue = deque([1])

        while queue:
            city = queue.popleft()
            for next_city, road in roads_dict[city]:
                if next_city not in visited_cities:
                    visited_cities.add(next_city)
                    queue.append(next_city)
                visited_roads.add(road)

        return min(visited_roads)
