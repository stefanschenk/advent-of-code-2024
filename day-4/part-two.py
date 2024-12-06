
puzzle = open('input').read().splitlines()

xMasCount = 0

for lineIdx, line in enumerate(puzzle):
    for charIdx, char in enumerate(line):
        if char == 'A':
            # M S  M M
            #  A    A
            # M S  S S
            try:
                if lineIdx >= 1 and charIdx >= 1:
                    diagonal1 = puzzle[lineIdx-1][charIdx-1] + puzzle[lineIdx+1][charIdx+1]
                    diagonal2 = puzzle[lineIdx+1][charIdx-1] + puzzle[lineIdx-1][charIdx+1]

                    diagonal3 = puzzle[lineIdx-1][charIdx+1] + puzzle[lineIdx+1][charIdx-1]

                    if (diagonal1 == 'MS' and diagonal2 == 'MS') or (diagonal1 == 'MS' and diagonal3 == 'MS'):
                        xMasCount += 1
            except IndexError:
                pass

            # S S  S M
            #  A    A
            # M M  S M
            try:
                if lineIdx >= 1 and charIdx >= 1:
                    diagonal1 = puzzle[lineIdx+1][charIdx+1] + puzzle[lineIdx-1][charIdx-1]
                    diagonal2 = puzzle[lineIdx+1][charIdx-1] + puzzle[lineIdx-1][charIdx+1]

                    diagonal3 = puzzle[lineIdx-1][charIdx+1] + puzzle[lineIdx+1][charIdx-1]

                    if (diagonal1 == 'MS' and diagonal2 == 'MS') or (diagonal1 == 'MS' and diagonal3 == 'MS'):
                        xMasCount += 1
            except IndexError:
                pass

print('X-MAS? ', xMasCount)