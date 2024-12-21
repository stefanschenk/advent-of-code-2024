# input = '0 1 10 99 999' # example 1
# input = '125 17' # example 2
from util import timed

input = '572556 22 0 528 4679021 1 10725 2790' # puzzle input

class Stone:
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value: int|None):
        self._index = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    def __init__(self, index: int|None, value: int):
        self.index = index
        self.value = value

    def __repr__(self):
        return repr(f"{self.index}:{self.value}")

    def __str__(self):
        return str(self.value)


def read_input(file = None):
    set_of_stones = []

    if file is None:
        set_of_stones = [Stone(i, int(v)) for i,v in enumerate(input.split(' '))]

    return set_of_stones

def apply_rule(stone: Stone, set_of_stones:list[Stone]) -> list[Stone]:

    def reindex(s):
        for idx, _s in enumerate(s):
            _s.index = idx
        return s

    if stone.value == 0:
        stone.value = 1
    elif len("%i" % stone.value) % 2 == 0:
        current_value = str(stone.value)
        left_value = int(current_value[0:int(len(current_value)/2)])
        right_value = int(current_value[int(len(current_value)/2):len(current_value)])

        stone.value = left_value
        set_of_stones.insert(stone.index+1, Stone(None, right_value))
        set_of_stones = reindex(set_of_stones)
    else:
        stone.value = stone.value * 2024

    return set_of_stones

@timed
def main():
    stones = read_input()

    for i in range(25):
        print('blink', i)
        for stone in stones.copy():
            apply_rule(stone, stones)

    print('Number of stones? ', len(stones)) # this takes around 15 mins to calculate


if __name__ == "__main__":
    main()