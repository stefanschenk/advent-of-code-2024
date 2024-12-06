
puzzle = open('input').read().splitlines()

xmasCount = 0

for lineIdx, line in enumerate(puzzle):
    # search horizontal
    xmasCount += line.count('XMAS')
    xmasCount += line.count('SAMX')

    # search vertical / diagonal
    for charIdx, char in enumerate(line):
        if char == 'X':
            # down
            try:
                mas = puzzle[lineIdx+1][charIdx] + puzzle[lineIdx+2][charIdx] + puzzle[lineIdx+3][charIdx]
                if mas == 'MAS':
                    xmasCount += 1
            except IndexError:
                pass

            # up
            try:
                if lineIdx >= 3:
                    mas = puzzle[lineIdx-1][charIdx] + puzzle[lineIdx-2][charIdx] + puzzle[lineIdx-3][charIdx]
                    if mas == 'MAS':
                        xmasCount += 1
            except IndexError:
                pass

            # diagonal down-right
            try:
                mas = puzzle[lineIdx+1][charIdx+1] + puzzle[lineIdx+2][charIdx+2] + puzzle[lineIdx+3][charIdx+3]
                if mas == 'MAS':
                    xmasCount += 1
            except IndexError:
                pass

            # diagonal down-left
            try:
                if charIdx >= 3:
                    mas = puzzle[lineIdx+1][charIdx-1] + puzzle[lineIdx+2][charIdx-2] + puzzle[lineIdx+3][charIdx-3]
                    if mas == 'MAS':
                        xmasCount += 1
            except IndexError:
                pass

            # diagonal up-left
            try:
                if lineIdx >= 3 and charIdx >= 3:
                    mas = puzzle[lineIdx-1][charIdx-1] + puzzle[lineIdx-2][charIdx-2] + puzzle[lineIdx-3][charIdx-3]
                    if mas == 'MAS':
                        xmasCount += 1
            except IndexError:
                pass

            # diagonal up-right
            try:
                if lineIdx >= 3 :
                    mas = puzzle[lineIdx-1][charIdx+1] + puzzle[lineIdx-2][charIdx+2] + puzzle[lineIdx-3][charIdx+3]
                    if mas == 'MAS':
                        xmasCount += 1
            except IndexError:
                pass

print('XMAS? ', xmasCount)