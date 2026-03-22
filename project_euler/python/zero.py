"""
Problem 0: Find the sum of the first 807,000 odd squares numbers.

Reasoning:

Just loop the odd numbers and sum their squares. The upper limit is 807,000, so we can loop from 1 to 807,000 with a step of 2 (to get only odd numbers) and sum their squares.

"""


def main() -> int:
    total = 0
    upper_limit = 807000

    for i in range(1, upper_limit, 2):
        total += i * i

    return total


if __name__ == "__main__":
    print(main())
