reports = []

with open('input') as file:
    for line in file:
        levelsIn = line.split(' ')

        levelsOut = []
        for level in levelsIn:
           levelsOut.append(int(level.rstrip()))

        reports.append(levelsOut)

print(len(reports)) # 1000

reports2 = reports.copy()

for idx, report in enumerate(reports):
    changes = []
    for idx2, level in enumerate(report):
        if idx2 > 0:
            changes.append('up' if level-report[idx2-1] > 0 else 'down')

    if not(changes.count('up') == len(changes) or changes.count('down') == len(changes)):
        reports2.remove(report)


print(len(reports2)) # 503

reports3 = reports2.copy()

for idx, report in enumerate(reports2):
    changes = []

    for idx2, level in enumerate(report):
        if idx2 > 0:
            changes.append(abs(level-report[idx2-1]))

    # list comprehension to check if step between levels is < 1 or > 3
    x = [i for i in changes if i>3 or i < 1]

    if len(x) > 0:
        reports3.remove(report)

print(len(reports3)) # 230
