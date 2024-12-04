# based on part-one
# but if the report is unsafe, safe the report to another array to process again


reports = []
safeReports = []
unsafeReports = []
reallyUnsafeReports = []

with open('input') as file:
    for line in file:
        levelsIn = line.split(' ')

        levelsOut = []
        for level in levelsIn:
            levelsOut.append(int(level.rstrip()))

        reports.append(levelsOut)

print(len(reports)) # 1000

def check_report(_report):
    changes = []
    levelChanges = []

    for idx2, level in enumerate(_report):
        if idx2 > 0:
            changes.append('up' if level-_report[idx2-1] > 0 else 'down')
            levelChanges.append(abs(level-_report[idx2-1]))

    if not(changes.count('up') == len(changes) or changes.count('down') == len(changes)):
        return False

    # list comprehension to check if step between levels is < 1 or > 3
    x = [i for i in levelChanges if i>3 or i < 1]

    if len(x) > 0:
        return False

    return True


while len(reports) > 0:
    report = reports.pop()

    if check_report(report):
        safeReports.append(report)
    else:
        unsafeReports.append(report)


print('SAFE: ', len(safeReports))
print('UNSAFE: ', len(unsafeReports))

while len(unsafeReports) > 0:
    unsafeReport = unsafeReports.pop()
    actuallySafe = False

    for idx, level in enumerate(unsafeReport):
        del unsafeReport[idx]

        if check_report(unsafeReport):
            actuallySafe = True
            break

        unsafeReport.insert(idx,level)

    if actuallySafe:
        safeReports.append(unsafeReport)
    else:
        reallyUnsafeReports.append(unsafeReport)

print('ACTUALLY SAFE: ', len(safeReports))
print('REALLY UNSAFE: ', len(reallyUnsafeReports))