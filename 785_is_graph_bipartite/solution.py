from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        unvisited_nodes = set(range(len(graph)))

        while len(unvisited_nodes) > 0:
            set_A = set()
            set_B = set()
            queue = []

            node = unvisited_nodes.pop()
            set_A.add(node)
            queue.append(node)
            while queue:
                node = queue.pop()
                unvisited_nodes.discard(node)
                if node in set_A:
                    for next_node in graph[node]:
                        if next_node in set_A:
                            return False
                        if next_node not in set_B:
                            set_B.add(next_node)
                            queue.append(next_node)
                else:
                    for next_node in graph[node]:
                        if next_node in set_B:
                            return False
                        if next_node not in set_A:
                            set_A.add(next_node)
                            queue.append(next_node)
            # if len(set_A) + len(set_B) < 2:
            #     return False

        return True
