from typing import Tuple
from unicodedata import digit


def parse_solution(file_input) -> int:
    result = -1

    with open(file=file_input, mode="r") as file:
        while line := file.readline():
            result = int(line)

    return result


def get_direction_and_distance(line) -> Tuple[str, int]:
    return line[0], int(line[1:])


def get_digit_pointed(digit_pointed: int, distance: int, direction: str) -> int:
    return digit_pointed + distance if direction == "R" else digit_pointed - distance


def test_cases(
    title: str,
    digit_pointed: int,
    input_file: str,
    solution_file_first: str,
    solution_file_second: str,
):
    old_password = first_solution(input_file, digit_pointed)
    solution = parse_solution(solution_file_first)

    assert old_password == solution, (
        f"The first solution for {title} doesn't match, should be {solution} but {old_password} is found"
    )

    new_password = second_solution(input_file, digit_pointed)
    solution = parse_solution(solution_file_second)

    assert new_password == solution, (
        f"The second solution for {title} doesn't match, should be {solution} but {new_password} is found"
    )


def first_solution(file_input, starting_digit) -> int:
    digit_pointed = starting_digit

    password = 0

    index = 1

    with open(file_input, "r") as file:
        while line := file.readline():
            direction, distance = get_direction_and_distance(line)

            digit_pointed = get_digit_pointed(digit_pointed, distance, direction)

            digit_pointed %= 100

            if digit_pointed == 0:
                password += 1

            index += 1

    return password


def second_solution(file_input, starting_digit) -> int:
    digit_pointed = starting_digit

    password = 0

    with open(file_input, "r") as file:
        while line := file.readline():
            direction, distance = get_direction_and_distance(line)

            for _ in range(distance):
                move_tile = 1 if direction == "R" else -1

                digit_pointed += move_tile
                digit_pointed = digit_pointed % 100

                if digit_pointed == 0 or digit_pointed == 100:
                    password += 1

    return password


if __name__ == "__main__":
    input_file = "input_sample.txt"
    input_solution_first = "input_sample_solution_first.txt"
    input_solution_second = "input_sample_solution_second.txt"

    DIGIT_POINTED = 50

    test_cases(
        "sample", DIGIT_POINTED, input_file, input_solution_first, input_solution_second
    )
    test_cases(
        "sandbox",
        DIGIT_POINTED,
        "input_sandbox.txt",
        "input_sandbox_solution_first.txt",
        "input_sandbox_solution_second.txt",
    )

    input_file = "input.txt"
    first_problem = first_solution(input_file, DIGIT_POINTED)
    second_problem = second_solution(input_file, DIGIT_POINTED)
    print(first_problem, second_problem)

    # print(old_password, password)
