from collections import deque
from typing import List

pipe_types = [
    [],
    [[-1, 0], [0, 1], [1, 0], [0, -1]], # up, right, down, left
    [[-1, 0], [1, 0]],
    [[0, 1], [0, -1]],
    [[-1, 0], [0, 1]],
    [[1, 0], [0, 1]],
    [[1, 0], [0, -1]],
    [[-1, 0], [0, -1]],
]

def is_valid_movement(old_x, old_y, new_x, new_y, new_pipe_type):
    # print(old_x, old_y, new_x, new_y, new_pipe_type)
    for dx, dy in pipe_types[new_pipe_type]:
        temp_x, temp_y = new_x + dx, new_y + dy
         # print(temp_x, temp_y)
        if temp_x == old_x and temp_y == old_y:
            return True

    return False


class Solution:
    def solve(self, n: int, m: int, x: int, y: int, l: int, pipe_map: List[List[int]]):

        global_row = n
        global_col = m
        global_endoscope_length = l

        visit = [[False] * m for _ in range(n)]

        def bfs(x, y, step):
            if visit[x][y] and pipe_map[x][y] != 0:
                return

            visit[x][y] = True

            q = deque([(x, y, step)])

            while q:
                x, y, step = q.popleft()
                pipe_type = pipe_map[x][y]
                pipe_directions = pipe_types[pipe_type]
                # print("hello")
                for dx, dy in pipe_directions:
                    temp_x, temp_y = x+dx, y+dy

                    if (temp_x in range(global_row) and temp_y in range(global_col)
                            and pipe_map[temp_x][temp_y] != 0
                            and not visit[temp_x][temp_y]
                            and is_valid_movement(x, y, temp_x, temp_y, pipe_map[temp_x][temp_y])
                            and step+1 <= global_endoscope_length):
                        # print((temp_x, temp_y, step+1))
                        q.append((temp_x, temp_y, step+1))
                        visit[temp_x][temp_y] = True


        bfs(x, y, 1)

        # print(visit)

        cell = 0
        for i in range(global_row):
            for j in range(global_col):
                if visit[i][j]:
                    cell += 1

        return cell


if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        n, m, x, y, l = input().strip().split()

        pipe_map = [[] for _ in range(int(n))]

        for i in range(int(n)):
            pipe_map[i] = [int(s) for s in input().strip().split()]

        # print(n, m, x, y, l)
        # print(pipe_map)

        solution = Solution()
        res = solution.solve(int(n), int(m), int(x), int(y), int(l), pipe_map)

        print(res)