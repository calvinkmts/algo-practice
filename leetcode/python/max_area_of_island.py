from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area_of_island = 0

        def traverse_map(row, col):
            if (row not in range(rows) or col not in range(cols)
                    or grid[row][col] == 0 or (row, col) in visit):
                return 0

            visit.add((row, col))

            area_size = 1

            directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
            for dir_row, dir_col in directions:
                temp_row, temp_col = row + dir_row, col + dir_col
                area_size += traverse_map(temp_row, temp_col)

            return area_size

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1 and (i, j) not in visit:
                    max_area_of_island = max(max_area_of_island, traverse_map(i, j))

        return max_area_of_island
