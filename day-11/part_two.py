from collections import Counter
from util import timed

# input = '0 1 10 99 999' # example 1
# input = '125 17' # example 2
input = '572556 22 0 528 4679021 1 10725 2790' # puzzle input

def read_input(file = None):
    set_of_stones = []

    if file is None:
        set_of_stones = [int(v) for v in input.split(' ')]

    return Counter(set_of_stones)

def apply_rule(stone: int, count: int, stones: dict):
    keys = []

    if stone == 0:
        keys = [1]
    elif len("%i" % stone) % 2 == 0:
        current_value = str(stone)
        left_value = int(current_value[0:int(len(current_value)/2)])
        right_value = int(current_value[int(len(current_value)/2):len(current_value)])
        keys = [left_value, right_value]
    else:
        keys = [stone*2024]

    for key in keys:
        current_count = stones.get(key, 0)
        stones[key] = current_count + count

@timed
def main():
    stones = read_input()

    for i in range(75):
        it_stones = dict()
        for k,v in stones.copy().items():
            apply_rule(k, v, it_stones)

        stones = it_stones

    print('answer? ', sum(stones.values()))

if __name__ == "__main__":
    main()