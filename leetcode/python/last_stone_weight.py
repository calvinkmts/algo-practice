import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = list(map(lambda x: -1 * x, stones))

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first_heaviest = heapq.heappop(max_heap) * -1
            second_heaviest = heapq.heappop(max_heap) * -1

            if first_heaviest != second_heaviest:
                new_value = abs((first_heaviest * -1) - (second_heaviest * -1))
                heapq.heappush(max_heap, new_value * -1)

        if len(max_heap) == 0:
            return 0

        return max_heap[0] * -1