from itertools import combinations

puzzle = list(map(lambda x:list(x), open('input').read().splitlines()))

# Save pairs in list, character and position
antennas: dict[str, list[tuple]] = dict()
antennaPairs = dict()

def scan_map():
    for idxRow, row in enumerate(puzzle):
        for idxCol, col in enumerate(row):
            if not col == '.':
                antennas.update({col: antennas.get(col, []) + [(idxRow, idxCol)]})

def detect_antenna_pairs():
    for k,v in antennas.items():
        antennaPairs[k] = list(combinations(v, 2))

def calculate_antinodes():
    antinodes = set() # use set() to prevent duplicates in list

    def calculate_distance(coord: tuple[tuple[int,int]]):
        return (
            coord[1][0] - coord[0][0],
            coord[1][1] - coord[0][1]
        )

    def sanitize(item):
        return not(item[0] < 0 or item[0] >= len(puzzle) or item[1] < 0 or item[1] >= len(puzzle[0]))

    for pair in antennaPairs.values():
        for pos in pair:
            distance = calculate_distance(pos)

            antinode_one = (pos[0][0] - distance[0], pos[0][1] - distance[1])
            antinode_two = (pos[1][0] + distance[0], pos[1][1] + distance[1])

            antinodes.update([antinode_one, antinode_two])

    return set(filter(sanitize, antinodes))

if __name__ == "__main__":
    scan_map()
    detect_antenna_pairs()
    antinodes = calculate_antinodes()

    print(len(antinodes))
