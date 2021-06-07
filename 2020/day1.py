
vals = set()
for line in open('day1input.txt', 'r'):
    if len(line.strip()) > 0:
        vals.add(int(line.strip()))

for val in vals:
    if (2020 - val) in vals:
        print val, 2020-val, val * (2020 - val)
