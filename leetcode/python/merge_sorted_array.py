from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[:] = nums1[:m] + nums2[:n]
    nums1.sort()
    # print(nums1)

if __name__ == "__main__":
    merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
