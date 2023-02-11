from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
            self,
            n: int,
            redEdges: List[List[int]],
            blueEdges: List[List[int]]
    ) -> List[int]:
        red_edges_dict = defaultdict(list)
        blue_edges_dict = defaultdict(list)
        for edge in redEdges:
            red_edges_dict[edge[0]].append(edge[1])
        for edge in blueEdges:
            blue_edges_dict[edge[0]].append(edge[1])

        result = [0]
        for i in range(1, n):
            result.append(-1)
        visited_red = set()
        visited_blue = set()
        queue = deque([(0, 0, '')])

        while queue:
            node, dist, prev_color = queue.popleft()
            if result[node] == -1:
                result[node] = dist
            elif result[node] > dist:
                result[node] = dist

            if prev_color != 'red' and node in red_edges_dict:
                for next_node in red_edges_dict[node]:
                    if next_node not in visited_red:
                        visited_red.add(next_node)
                        queue.append((next_node, dist + 1, 'red'))

            if prev_color != 'blue' and node in blue_edges_dict:
                for next_node in blue_edges_dict[node]:
                    if next_node not in visited_blue:
                        visited_blue.add(next_node)
                        queue.append((next_node, dist + 1, 'blue'))

        return result
