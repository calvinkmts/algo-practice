import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]

            heapq.heappush(max_heap, (dist*-1, point))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        solution = [point[1] for point in max_heap]

        return solution