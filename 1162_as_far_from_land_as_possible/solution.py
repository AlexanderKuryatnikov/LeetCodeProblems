from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        reached_tiles = set()
        distance = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    reached_tiles.add((i, j))

        while len(reached_tiles) > 0:
            next_reached_tiles = set()
            for tile in reached_tiles:
                i, j = tile
                for next_i, next_j in {(i + 1, j),
                                       (i - 1, j),
                                       (i, j + 1),
                                       (i, j - 1)}:
                    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                        if grid[next_i][next_j] == 0:
                            grid[next_i][next_j] = distance + 3
                            next_reached_tiles.add((next_i, next_j))
            reached_tiles = next_reached_tiles
            distance += 1

        if distance <= 0:
            return -1
        return distance
