from collections import defaultdict
from typing import List, Optional


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.city_roads = defaultdict(set)
        for city1, city2 in roads:
            self.city_roads[city1].add(city2)
            self.city_roads[city2].add(city1)

        self.seats = seats
        self.cost = 0
        self.calculate_next_node(city=0)

        return self.cost

    def calculate_next_node(
            self,
            city: int,
            prev_city: Optional[int] = None
    ) -> None:
        reprs = 1
        for next_city in self.city_roads[city]:
            if next_city == prev_city:
                continue
            next_reprs = self.calculate_next_node(
                city=next_city,
                prev_city=city
            )
            self.cost += (next_reprs + self.seats - 1) // self.seats
            reprs += next_reprs

        return reprs
