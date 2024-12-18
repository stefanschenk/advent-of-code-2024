from itertools import chain
from multiprocessing import Pool
from util import timed

# input = '0 1 10 99 999' # example 1
# input = '125 17' # example 2
input = '572556 22 0 528 4679021 1 10725 2790' # puzzle input

def read_input(file = None):
    set_of_stones = []

    if file is None:
        set_of_stones = [int(v) for v in input.split(' ')]

    return set_of_stones

def apply_rule(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len("%i" % stone) % 2 == 0:
        current_value = str(stone)
        left_value = int(current_value[0:int(len(current_value)/2)])
        right_value = int(current_value[int(len(current_value)/2):len(current_value)])

        return [left_value, right_value]
    else:
        return [stone*2024]

@timed
def main():
    stones = read_input()

    for i in range(30):
        with Pool(2) as p:
            res = p.map(apply_rule, stones)
        p.close()

        stones = list(chain.from_iterable(res))

    print('Number of stones? ', len(stones)) # this takes around 2.5 seconds

if __name__ == "__main__":
    main()