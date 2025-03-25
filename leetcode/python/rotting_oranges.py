import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        rotten_oranges = collections.deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))
                    visited.add((i, j))

        print(rotten_oranges)

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        while rotten_oranges:
            row, col, minute = rotten_oranges.popleft()

            res = max(res, minute)

            grid[row][col] = 2

            for dir_r, dir_c in dirs:
                new_r = dir_r + row
                new_c = dir_c + col

                if (new_r in range(rows) and new_c in range(cols)
                        and (new_r, new_c) not in visited
                        and grid[new_r][new_c] == 1):

                    visited.add((new_r, new_c))
                    rotten_oranges.append((new_r, new_c, minute+1))

        fresh_oranges_left = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges_left += 1

        if fresh_oranges_left > 0:
            return -1

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting([[2,2],[1,1],[0,0],[2,0]]))