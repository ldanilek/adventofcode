
vals = set()
for line in open('day1input.txt', 'r'):
    if len(line.strip()) > 0:
        vals.add(int(line.strip()))

for val in vals:
    for val2 in vals:
        val3 = 2020 - val - val2
        if val3 in vals:
            print val, val2, val3, val * val2 * val3
