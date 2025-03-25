from typing import List, Dict, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        visited = set()

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        is_found = False

        def traverse(r: int, c: int, q: str):
            nonlocal is_found

            if is_found:
                return

            if (r, c) in visited:
                return

            if r not in range(rows) or c not in range(cols):
                return

            if board[r][c] != q[0]:
                return

            if len(q) == 1 and q[0] == board[r][c]:
                is_found |= True
                return

            visited.add((r, c))

            for d_row, d_col in dirs:
                new_row = r + d_row
                new_col = c + d_col

                traverse(new_row, new_col, q[1:])

            visited.remove((r, c))

        for i in range(rows):
            for j in range(cols):

                if board[i][j] == word[0]:
                    traverse(i, j, word)

        return is_found
