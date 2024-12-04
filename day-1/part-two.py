arr1 = []
arr2 = []

tab = '   '

with open('input') as file_2:
    for line in file_2:
        locs = line.split(tab)
        arr1.append(locs[0].rstrip())
        arr2.append(locs[1].rstrip())

similarityScore = 0

for loc in arr1:
    locCount = arr2.count(loc)
    if locCount > 0:
        similarityScore += int(loc)*locCount

print(similarityScore)

