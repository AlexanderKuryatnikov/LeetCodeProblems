from collections import deque
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        city_roads = {}
        for city1, city2 in roads:
            if city1 in city_roads:
                city_roads[city1][1].add(city2)
            else:
                city_roads[city1] = [1, {city2}]
            if city2 in city_roads:
                city_roads[city2][1].add(city1)
            else:
                city_roads[city2] = [1, {city1}]

        cost = 0
        queue = deque()
        for city, cities in city_roads.items():
            if len(cities[1]) == 1:
                queue.append(city)

        while queue:
            city = queue.popleft()
            if city == 0 and len(city_roads[city][1]) == 0:
                break
            elif len(city_roads[city][1]) != 1 or city == 0:
                queue.append(city)
                continue
            reprs = city_roads[city][0]
            next_city = city_roads[city][1].pop()
            city_roads[next_city][0] += reprs
            city_roads[next_city][1].remove(city)
            cost += (reprs + seats - 1) // seats
            queue.append(next_city)

        return cost
