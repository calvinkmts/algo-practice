from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_len = len(matrix)
        col_len = len(matrix[0])

        bottom_row = 0
        top_row = row_len - 1

        found_row = -1
        while bottom_row <= top_row:
            mid_row = (bottom_row + top_row) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][col_len - 1]:
                found_row = mid_row
                break
            elif target < matrix[mid_row][0]:
                top_row = mid_row - 1
            elif target > matrix[mid_row][col_len - 1]:
                bottom_row = mid_row + 1

        if found_row >= 0:
            left = 0
            right = col_len - 1

            while left <= right:
                mid = (left + right) // 2

                if target == matrix[found_row][mid]:
                    return True
                elif target > matrix[found_row][mid]:
                    left = mid + 1
                elif target < matrix[found_row][mid]:
                    right = mid - 1

        return False

if __name__ == "__main__":

    solution = Solution()
    solution.searchMatrix([[1]], 1)
