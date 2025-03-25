from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        vertex_occurrence = {}

        for i, j in edges:

            if i not in vertex_occurrence:
                vertex_occurrence[i] = 0
            else:
                vertex_occurrence[i] += 1

            if j not in vertex_occurrence:
                vertex_occurrence[j] = 0
            else:
                vertex_occurrence[j] += 1

        res = -1
        node_length = len(vertex_occurrence.items())
        for node, occurrence in vertex_occurrence.items():
            if occurrence == node_length - 1:
                res = node

        return res