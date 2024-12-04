import re

lines = []
mulPattern = re.compile("mul\((?P<a>\d+),(?P<b>\d+)\)")

# Example
example = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
exampleCalc = mulPattern.findall(example)

exampleResult = 0
for calc in exampleCalc:
    exampleResult += int(calc[0]) * int(calc[1])

print(exampleResult) # 161

# Part One
result = 0

with open('input') as file:
    for line in file:
        lines.append(line)

while len(lines) > 0:
    line = lines.pop()

    calculations = mulPattern.findall(line)

    for calculation in calculations:
        result += int(calculation[0]) * int(calculation[1])

print('multiplications? ', result)