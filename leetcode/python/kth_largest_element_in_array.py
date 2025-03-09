import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, pointer = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1
            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer < k:
                return quickSelect(pointer + 1, r)
            elif pointer > k:
                return quickSelect(l, pointer - 1)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #
    #     max_heap = []
    #
    #     for num in nums:
    #         heapq.heappush(max_heap, num)
    #
    #         if len(max_heap) > k:
    #             heapq.heappop(max_heap)
    #
    #     return max_heap[0]