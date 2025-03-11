class Solution:
    def hammingWeight(self, n: int) -> int:

        bit_set_counter = 0

        while n > 0:
            if n % 2 == 1:
                bit_set_counter += 1

            n = n // 2

        return bit_set_counter
