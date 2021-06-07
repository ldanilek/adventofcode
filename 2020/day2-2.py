import re

regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

count_valid = 0
for line in open('day2input.txt', 'r'):
    if len(line.strip()) > 0:
        [index1, index2, letter, password] = re.match(regex, line.strip()).groups()
        [match1, match2] = [int(password[int(index)-1] == letter) for index in (index1, index2)]
        count_valid += match1 ^ match2

print(count_valid)
