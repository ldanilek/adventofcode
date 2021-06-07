
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

print(slope(3, 1))

