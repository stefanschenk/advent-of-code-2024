
guard = '^'
obstruction = '#'

puzzle = list(map(lambda x:list(x), open('input').read().splitlines()))

positions = []
currentRow = 0
currentCol = 0

# Find guard
for idxRow, row in enumerate(puzzle):
    for idxCol, column in enumerate(row):
        if column == guard:
            currentRow = idxRow
            currentCol = idxCol
            positions.append((currentRow, currentCol))

guardExit = False
direction = 'UP'

while not guardExit:
    try:
        match direction:
            case 'UP':
                while direction == 'UP':
                    if puzzle[currentRow-1][currentCol] == obstruction:
                        direction = 'RIGHT'
                    else:
                        currentRow -= 1
                        positions.append((currentRow, currentCol))
            case 'RIGHT':
                while direction == 'RIGHT':
                    if puzzle[currentRow][currentCol+1] == obstruction:
                        direction = 'DOWN'
                    else:
                        currentCol += 1
                        positions.append((currentRow, currentCol))
            case 'DOWN':
                while direction == 'DOWN':
                    if puzzle[currentRow+1][currentCol] == obstruction:
                        direction = 'LEFT'
                    else:
                        currentRow += 1
                        positions.append((currentRow, currentCol))
            case 'LEFT':
                while direction == 'LEFT':
                    if puzzle[currentRow][currentCol-1] == obstruction:
                        direction = 'UP'
                    else:
                        currentCol -= 1
                        positions.append((currentRow, currentCol))

        if currentRow == -1 or currentCol == -1:
            guardExit = True
    except IndexError:
        guardExit = True

print('STEPS? ', len(set(positions)))