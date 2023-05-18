from typing import List


class Solution:
    def findSmallestSetOfVertices(
            self,
            n: int,
            edges: List[List[int]]
    ) -> List[int]:
        nodes_reached = set()

        for edge in edges:
            nodes_reached.add(edge[1])

        unreachable_nodes = []
        for i in range(n):
            if i not in nodes_reached:
                unreachable_nodes.append(i)

        return unreachable_nodes
