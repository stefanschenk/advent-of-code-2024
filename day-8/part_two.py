from part_one import antennas, antennaPairs, scan_map, detect_antenna_pairs, puzzle

maxX = len(puzzle)
maxY = len(puzzle[0])

def calculate_antinodes():
    antinodes = set() # use set() to prevent duplicates in list

    def calculate_distance(coord: tuple[tuple[int,int]]):
        return (
            coord[1][0] - coord[0][0],
            coord[1][1] - coord[0][1]
        )

    def in_bound(x, y):
        return 0 <= x <= maxX and 0 <= y <= maxY

    def sanitize(item):
        return not(item[0] < 0 or item[0] >= len(puzzle) or item[1] < 0 or item[1] >= len(puzzle[0]))

    for pair in antennaPairs.values():
        for pos in pair:
            distance = calculate_distance(pos)

            x1 = pos[0][0] - distance[0]
            y1 = pos[0][1] - distance[1]
            x2 = pos[1][0] + distance[0]
            y2 = pos[1][1] + distance[1]

            while in_bound(x1, y1):
                antinodes.add((x1, y1))
                x1 -= distance[0]
                y1 -= distance[1]

            while in_bound(x2, y2):
                antinodes.add((x2, y2))
                x2 += distance[0]
                y2 += distance[1]

    return set(filter(sanitize, antinodes))

if __name__ == "__main__":
    scan_map()
    detect_antenna_pairs()
    antinodes = calculate_antinodes()

    for k,v in antennas.items():
        if len(v) > 1:
            antinodes.update(v)

    print(len(antinodes))