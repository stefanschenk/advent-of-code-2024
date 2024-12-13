from itertools import product

puzzle = list(map(lambda x:list(x), open('input').read().splitlines()))

def find_height_points(height_map, height_point) -> list[tuple[int, int]]:
    positions = []

    for posX, section in enumerate(height_map):
        for posY, height in enumerate(section):
            if height == str(height_point): positions.append((posX,posY))

    return sorted(positions)

def find_trails(height_map):
    trails = list(product(find_height_points(height_map, 0))) # all trails start at a trailhead

    # find next point and update trails accordingly if next point is next to last point
    for x in range(1,10):
        intermediate = []

        for point in find_height_points(height_map, x):
            for trail in trails:
                [posX, posY] = trail[-1]

                if [(posX-1, posY), (posX+1, posY), (posX, posY-1), (posX, posY+1)].count(point) == 1:
                    trail += (point,)
                    intermediate.append(trail)

        trails = intermediate

    return trails

def score_trails(trails, routes):
    trail_score = 0

    for route in routes:
        for trail in trails:
            trail_route = (trail[0], trail[-1])

            if trail_route == route:
                trail_score += 1
                break

    return trail_score


if __name__ == "__main__":
    trailheads = find_height_points(puzzle, 0)
    endpoints = find_height_points(puzzle, 9)
    all_routes = list(product(trailheads, endpoints))

    possible_trails = find_trails(puzzle)

    score = score_trails(possible_trails, all_routes)

    print('Score? ', score)
    print('Trailrating? ', print(len(possible_trails))) # part 2 answer