import math

rows = []
for line in open('day3input.txt', 'r'):
    if len(line.strip()) > 0:
        rows.append(line.strip())

def slope(sx, sy):
    (x, y) = (0, 0)
    trees = 0
    while y < len(rows):
        trees += int(rows[y][x] == '#')
        x = (x + sx) % len(rows[y])
        y = (y + sy)

    return trees

vals = [slope(sx, sy) for (sx, sy) in 
    (
       (1, 1),
       (3, 1),
       (5, 1),
       (7, 1),
       (1, 2) 
    )]

p = 1
for val in vals:
    p *= val

print(p)

