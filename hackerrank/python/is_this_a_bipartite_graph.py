import collections
from typing import Tuple, List


def create_adj_list(n: int, edges: List[Tuple[int, int]]) -> List[List[int]]:

    adj_list = [[] for _ in range(n)]

    for i, j in edges:
        adj_list[i].append(j)

    return adj_list


class Solution:

    def solve(self, adj_list: List[List[int]]) -> bool:

        for neighbors in adj_list:
            if len(neighbors) < 1:
                return False

        return True



if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n, m = [int(x) for x in input().split()]

        edges = []
        for _ in range(m):
            i, j = [int(x) - 1 for x in input().split()]
            edges.append((i,j))
            edges.append((j,i))

        solution = Solution()

        adj_list = create_adj_list(n, edges)

        res = solution.solve(adj_list)

        if res:
            print("YES")
        else:
            print("NO")