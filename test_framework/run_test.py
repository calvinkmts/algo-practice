import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Test Framework Runner",
        description="This CLI tool is used to make solving coding challenges easier",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Advent of Code command
    aoc_parser = subparsers.add_parser("aoc", help="Run Advent of Code tests")
    aoc_parser.add_argument("run", help="Run the specified day's challenge")

    # Future: LeetCode command
    leetcode_parser = subparsers.add_parser("lc", help="Run LeetCode tests")
    leetcode_parser.add_argument("lc", help="Run the specified problem's challenge")

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
