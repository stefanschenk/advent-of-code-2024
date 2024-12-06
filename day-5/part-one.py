
puzzle = open('input').read().splitlines()

splitIndex = puzzle.index('')

orderingRules = list(map(lambda x:x.split('|'), puzzle[:splitIndex]))
updates = puzzle[splitIndex+1:]

pageNumberSum = 0

for update in updates:
    updateCorrect = True
    pages = update.split(',')

    for rule in orderingRules:
        if pages.count(rule[0]) > 0 and pages.count(rule[1]) > 0:
            if not pages.index(rule[1]) > pages.index(rule[0]):
                updateCorrect = False
                break

    if updateCorrect:
        pageNumberSum += int(pages[len(pages) // 2])

print('SUM? ', pageNumberSum)