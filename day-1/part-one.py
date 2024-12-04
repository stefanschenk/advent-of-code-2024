arr1 = []
arr2 = []
result = []

tab = '   '

with open('input') as file:
    for line in file:
        locs = line.split(tab)
        arr1.append(int(locs[0].rstrip()))
        arr2.append(int(locs[1].rstrip()))

arr1.sort()
arr2.sort()
arr2.reverse()

for l in arr1:
    result.append(abs(l-arr2.pop()))

distance = 0
for r in result:
    distance += r

print(distance)
