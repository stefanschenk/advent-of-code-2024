import re

lines = []
mulPattern = re.compile("mul\(\d+,\d+\)|do\(\)|don't\(\)")

# Example
example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
exampleCalc = mulPattern.findall(example)

exampleResult = 0
doExampleMultiplication = True
for calc in exampleCalc:
    if calc == "don't()":
        doExampleMultiplication = False
    elif calc == "do()":
        doExampleMultiplication = True
    else:
        if doExampleMultiplication:
            x,y = map(int, calc[4:-1].split(','))
            exampleResult += x*y

print(exampleResult) # 161

# Part Two
result = 0
doMultiplication = True

matches = re.findall(mulPattern, open('input').read())

for match in matches:
    if match == "don't()":
        doMultiplication = False
    elif match == "do()":
        doMultiplication = True
    else:
        if doMultiplication:
            x,y = map(int, match[4:-1].split(','))
            result += x*y

print('multiplications? ', result)
