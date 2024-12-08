from itertools import product
from operator import mul,add

puzzle = open('input').read().splitlines()
calibrationResult = 0

# only operators are * and +, always calculate from left to right, no operator precedence
for line in puzzle:
    [result, digits] = line.split(':')

    digits = list(map(lambda x:int(x), digits.strip().split(' ')))
    result = int(result)

    x = [mul,add]
    operations = [p for p in product(x, repeat=len(digits)-1)]

    for entry in operations:
        total = 0
        for idx, calculation in enumerate(entry):
            if idx == 0:
                total = calculation(digits[idx],digits[idx+1])
            else:
                total = calculation(total, digits[idx+1])

        if total == result:
            calibrationResult += total
            break

print('Calibration result? ', calibrationResult)