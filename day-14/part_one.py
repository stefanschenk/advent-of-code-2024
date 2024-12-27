import re
from math import floor, prod

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

def move_robot(robot, final_positions):
    (pos_x, pos_y) = robot[0]
    (mov_x, mov_y) = robot[1]

    # print(pos_x, pos_y)
    for _ in range(100):
        pos_x += mov_x #boundary_width
        pos_y += mov_y #boundary_length

        if pos_x < 0: pos_x = boundary_width + pos_x + 1
        if pos_x > boundary_width: pos_x = pos_x - boundary_width - 1

        if pos_y < 0: pos_y = boundary_length + pos_y + 1
        if pos_y > boundary_length: pos_y = pos_y - boundary_length - 1

    final_positions.append((pos_x, pos_y))

def filter_positions(positions, filtered_positions):
    filter_x = floor(boundary_width/2)
    filter_y = floor(boundary_length/2)

    while positions:
        (pos_x, pos_y) = positions.pop()

        if 0 <= pos_x < filter_x and 0 <= pos_y < filter_y:
            filtered_positions['q1'] += 1
        elif filter_x < pos_x <= boundary_width and 0 <= pos_y < filter_y:
            filtered_positions['q2'] += 1
        elif 0 <= pos_x < filter_x and filter_y < pos_y <= boundary_length:
            filtered_positions['q3'] += 1
        elif filter_x < pos_x <= boundary_width and filter_y < pos_y <= boundary_length:
            filtered_positions['q4'] += 1


boundary_width = 101-1
boundary_length = 103-1

@timed
def main():
    robots = read_input('input')

    final_positions = []
    for robot in robots:
        move_robot(robot, final_positions)

    filtered_positions = {'q1':0, 'q2':0, 'q3':0,'q4':0}
    filter_positions(final_positions, filtered_positions)

    print(prod(filtered_positions.values()))


if __name__ == "__main__":
    main()