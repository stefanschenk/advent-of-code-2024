import re

from util import timed

puzzle_input = ''

def read_input(file = None):
    instructions = []

    if file is None:
        input_lines = puzzle_input
    else:
        input_lines = open(file).readlines()

    a = ()
    for input_line in input_lines:
        if input_line == '\n':
            instructions.append(a)
            a = ()
            continue

        a += tuple([int(x) for x in re.compile('(\\d+)').findall(input_line)])
    instructions.append(a)

    return instructions

def process_instructions(instruction, solutions):
    (a1, a2, b1, b2, r1, r2) = instruction
    r1 = 10_000_000_000_000 + r1
    r2 = 10_000_000_000_000 + r2

    print(f'1st equation: {a1}*x + {b1}*y = {r1}')
    print(f'1st equation: {a1}*x = {r1} - {b1}*y')
    print(f'1st equation: x = {r1/a1} - {b1/a1}*y')

    print(f'2nd equation: {a2}*x + {b2}*y = {r2}')
    print(f'2nd equation: {a2}*({r1/a1} - {b1/a1}*y) + {b2}*y = {r2}')
    print(f'2nd equation: {a2*(r1/a1)} - {a2*(b1/a1)}*y) + {b2}*y = {r2}')
    print(f'2nd equation: -{a2*(b1/a1)}*y + {b2}*y = {r2-(a2*(r1/a1))}')
    print(f'2nd equation: {b2+(-1*(a2*(b1/a1)))}*y = {r2-(a2*(r1/a1))}')
    print(f'2nd equation: y = {(r2-(a2*(r1/a1)))/(b2+(-1*(a2*(b1/a1))))}')

    print(f'1st equation: x = {(r1/a1)-((b1/a1)*((r2-(a2*(r1/a1)))/(b2+(-1*(a2*(b1/a1))))))}')
    print('<<<=====>>>')

    y = (r2-(a2*(r1/a1)))/(b2+(-1*(a2*(b1/a1))))
    x = (r1/a1)-((b1/a1)*((r2-(a2*(r1/a1)))/(b2+(-1*(a2*(b1/a1))))))

    if round(x, 3).is_integer() and round(y, 3).is_integer():
        solutions.append((round(x), round(y)))

@timed
def main():
    instructions = read_input('input')

    solutions = []
    [process_instructions(instruction, solutions) for instruction in instructions]

    tokens = 0
    for solution in solutions:
        tokens += solution[0]*3 + solution[1]*1

    print('Answer? ', tokens)

if __name__ == "__main__":
    main()