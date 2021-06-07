vf = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def valid_fields(fields):
    return all(v in fields for v in vf)

count_valid = 0
fields = set()
for line in open('day4input.txt', 'r'):
    if len(line.strip()) == 0:
        count_valid += int(valid_fields(fields))
        fields = set()
        continue

    fields.update(p.split(':')[0] for p in line.strip().split())

count_valid += int(valid_fields(fields))
print(count_valid)
