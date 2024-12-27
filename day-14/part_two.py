import re
from functools import cache

from util import timed

puzzle_input = ''

def read_input(file = None):
    robot_pv_list = []

    if file is None:
        input_lines = puzzle_input
    else:
        input_lines = open(file).readlines()

    pv_list = []
    for input_line in input_lines:
        pv_list.extend(re.compile("p=(\\d+,\\d+)\\sv=(-?\\d+,-?\\d+)").findall(input_line))

    for pv in pv_list:
        (position, velocity) = pv
        position = tuple([int(x) for x in position.split(',')])
        velocity = tuple([int(x) for x in velocity.split(',')])

        robot_pv_list.append((position, velocity))

    return robot_pv_list

@cache
def move_robot(seconds, robot):
    (pos_x, pos_y) = robot[0]
    (mov_x, mov_y) = robot[1]

    # print(pos_x, pos_y)
    for _ in range(seconds):
        pos_x += mov_x #boundary_width
        pos_y += mov_y #boundary_length

        if pos_x < 0: pos_x = boundary_width + pos_x + 1
        if pos_x > boundary_width: pos_x = pos_x - boundary_width - 1

        if pos_y < 0: pos_y = boundary_length + pos_y + 1
        if pos_y > boundary_length: pos_y = pos_y - boundary_length - 1

    return pos_x, pos_y

def print_line(line: list, output_file = None):
    line_to_print = ''
    line.sort()
    for i in range(boundary_width):
        if line.count(i) > 0:
            line_to_print = line_to_print + 'X'
        else:
            line_to_print = line_to_print + '.'

    if output_file is None:
        print(line_to_print)
    else:
        output_file.write(line_to_print)
        output_file.write('\n')
        output_file.flush()

boundary_width = 101-1
boundary_length = 103-1

@timed
def main():
    seconds = 8053
    # 8053 prints a line of consecutive robots
    is_easter_egg = False
    is_possible_easter_egg = False
    robots = read_input('input')

    with open('output', 'a') as output_file:
        while not is_easter_egg:
            # seconds += 1
            print(f'iteration {seconds}')

            final_positions = dict()
            for robot in robots:
                (end_pos_x, end_pos_y) = move_robot(seconds, robot)
                robots_in_row = final_positions.get(end_pos_x, [])
                robots_in_row.append(end_pos_y)
                final_positions[end_pos_x] = robots_in_row

            for line in range(boundary_length):
                if len(final_positions.get(line, [])) >= 30:
                    print('possible easter egg found!')
                    print(f'after {seconds} seconds')
                    # output_file.write(f'{seconds}:')
                    # print_line(final_positions.get(line, []), output_file)
                    is_possible_easter_egg = True
                    break


            if is_possible_easter_egg:
                is_easter_egg = True
                for line in range(boundary_length):
                    print_line(final_positions.get(line, []))
                break

if __name__ == "__main__":
    main()