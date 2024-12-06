
puzzle = open('input').read().splitlines()

splitIndex = puzzle.index('')

orderingRules = list(map(lambda x:x.split('|'), puzzle[:splitIndex]))
updates = puzzle[splitIndex+1:]

incorrectUpdates = []
pageNumberSum = 0

# First create list of incorrect updates
for update in updates:
    updateCorrect = True
    pages = update.split(',')

    for rule in orderingRules:
        if pages.count(rule[0]) > 0 and pages.count(rule[1]) > 0:
            if not pages.index(rule[1]) > pages.index(rule[0]):
                incorrectUpdates.append(pages)
                break

# Then loop through incorrect updates to correct the sequence
for pages in incorrectUpdates:
    rulesChecked = False

    while not rulesChecked:
        for idx, rule in enumerate(orderingRules):
            if pages.count(rule[0]) > 0 and pages.count(rule[1]) > 0:
                indexPageA = pages.index(rule[0])
                indexPageB = pages.index(rule[1])

                if not indexPageB > indexPageA:
                    pageA = pages.pop(indexPageA)
                    pages.insert(indexPageB, pageA)
                    break

            if idx == len(orderingRules)-1:
                rulesChecked = True

    pageNumberSum += int(pages[len(pages) // 2])

print('SUM? ', pageNumberSum)