import re

def m(regex, *preds):
    r = re.compile(regex)
    def matcher(s):
        m = r.match(s)
        return bool(
            m and (not m.groups() or any(
                g and preds[i](int(g)) for i, g in enumerate(m.groups())
            ))
        )

    return matcher

vf = {
    'byr': m(r'(\d\d\d\d)', lambda x: 1920 <= x <= 2002),
    'iyr': m(r'(\d\d\d\d)', lambda x: 2010 <= x <= 2020),
    'eyr': m(r'(\d\d\d\d)', lambda x: 2020 <= x <= 2030),
    'hgt': m(r'(\d+)cm|(\d+)in', lambda x: 150 <= x <= 193, lambda x: 59 <= x <= 76),
    'hcl': m(r'#[0-9a-f]{6}'),
    'ecl': m(r'amb|blu|brn|gry|grn|hzl|oth'),
    'pid': m(r'[0-9]{9}'),
    }

def valid_fields(fields):
    return all(v in fields and m(fields[v]) for v, m in vf.items())

count_valid = 0
fields = dict()
for line in open('day4input.txt', 'r'):
    if len(line.strip()) == 0:
        count_valid += int(valid_fields(fields))
        fields = dict()
        continue

    fields.update({p.split(':')[0]: p.split(':')[1] for p in line.strip().split()})

count_valid += int(valid_fields(fields))
print(count_valid)
