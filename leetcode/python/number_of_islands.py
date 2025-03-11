import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        number_of_islands = 0

        def visit_island(row, col):
            q = collections.deque()

            visit.add((row, col))

            q.append((row, col))

            while q:
                row, col = q.popleft()
                # down, left, up, right
                directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
                for dir_row, dir_col in directions:
                    temp_row, temp_col = dir_row + row, dir_col + col
                    if (temp_row in range(rows) and temp_col in range(cols)
                            and grid[temp_row][temp_col] == "1" and (temp_row, temp_col) not in visit):
                        visit.add((temp_row, temp_col))
                        q.append((temp_row, temp_col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    number_of_islands += 1
                    visit_island(i, j)

        return number_of_islands

