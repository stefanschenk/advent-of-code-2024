from functools import reduce

from util import timed

puzzle_input = ''
walls = []
boxes = []
moves = []
start_position = (0,)

def read_input(file = None):
    global start_position
    read_moves = False

    if file is None:
        input_lines = puzzle_input
    else:
        input_lines = open(file).readlines()

    for row_idx, input_line in enumerate(input_lines):
        if input_line == '\n':
            read_moves = True
            continue

        if read_moves:
            read_moves_input([*input_line])

        for col_idx, char in enumerate(input_line):
            if char == '#':
                walls.append((row_idx, col_idx))
            elif char == 'O':
                boxes.append((row_idx, col_idx))
            elif char == '@':
                start_position = (row_idx, col_idx)

def read_moves_input(moves_list):
    for move in moves_list:
        match move:
            case '<':
                moves.append((0, -1))
            case '^':
                moves.append((-1, 0))
            case '>':
                moves.append((0, 1))
            case 'v':
                moves.append((1, 0))

def move_robot():
    robot_position = start_position

    for move in moves:
        next_position = tuple(map(lambda x, y: x + y, robot_position, move))

        if walls.count(next_position) == 1:
            print('Ran into a wall, "Ouch!"')
            continue

        if boxes.count(next_position) == 1:
            print('Found a box, "Let\'s try to give it a push"')
            if not push_box(next_position, move):
                continue

        robot_position = next_position
        print(f'>>{robot_position}')

    return robot_position

def push_box(location, move):
    box = boxes.pop(boxes.index(location))
    next_position = tuple(map(lambda x, y: x + y, box, move))

    if walls.count(next_position) == 1:
        print('I cannot push this box through a wall, tag it as stationary')
        boxes.append(box)
        return False

    if boxes.count(next_position) == 1:
        print('Found another box, "Let\'s try to give that also a push"')
        if push_box(next_position, move):
            boxes.append(next_position)
            return True
        else:
            boxes.append(box)
            return False

    boxes.append(next_position)
    return True

@timed
def main():
    read_input('input')

    print(start_position)
    print('End position?', move_robot())

    print('Sum of GPS positions?', sum([reduce(lambda x, y: 100 * x + y, tpl) for tpl in boxes]))



if __name__ == "__main__":
    main()