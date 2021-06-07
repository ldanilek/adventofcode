import re

regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

count_valid = 0
for line in open('day2input.txt', 'r'):
    if len(line.strip()) > 0:
        [minimum, maximum, letter, password] = re.match(regex, line.strip()).groups()
        count = sum(int(l == letter) for l in password)
        count_valid += int(int(minimum) <= count <= int(maximum))

print(count_valid)
