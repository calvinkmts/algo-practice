from typing import Tuple


def get_direction_and_distance(line) -> Tuple[str, int]:
    return line[0], int(line[1:])

def first_solution(file_input, starting_digit) -> int:

    digit_pointed = starting_digit

    password = 0

    with open(input_file, 'r') as file: 

        while line := file.readline():

            direction, distance = get_direction_and_distance(line)

            digit_pointed = digit_pointed + distance if direction == 'R' else digit_pointed - distance 

            digit_pointed %= 100

            if digit_pointed == 0:
                password += 1

    return password


def second_solution(file_input, starting_digit) -> int:

    digit_pointed = starting_digit

    password = 0

    with open(file_input, 'r') as file:

        while line := file.readline():

            direction, distance = get_direction_and_distance(line)

            


    return password


if __name__ == "__main__":
    
    input_file = "input.txt"

    digit_pointed = 50
    
    password = first_solution(input_file, digit_pointed)

    print(password)
