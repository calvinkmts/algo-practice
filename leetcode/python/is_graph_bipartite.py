from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        odd = [0 for _ in range(len(graph))]

        def bfs(i):
            if odd[i]:
                return True
            q = deque([i])
            odd[i] = -1

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if odd[neighbor] == odd[node]:
                        return False
                    elif not odd[neighbor]:
                        q.append(neighbor)
                        odd[neighbor] = -1 * odd[node]
            return True

        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True