lines = open("../input.txt", 'r').readlines()

class Passport:
    def __init__(self, data):
        self.data = data
        self.fields = self.parse()
    
    def __str__(self):
        return str(self.fields)

    def parse(self):
        fields = {}
        for line in self.data:
            pieces = line.strip().split()
            for p in pieces:
                k, v = p.split(":")
                fields[k] = v
        return fields

    def is_valid(self):
        fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for r in required:
            if r not in self.fields:
                return False
        return True

def get_passports():
    temp = []
    passports = []
    for l in lines:
        if not l.strip():
            passports.append(Passport(temp))
            temp = []
        else:
            temp.append(l.strip())
    if temp:
        passports.append(Passport(temp))
    return passports

passports = get_passports()
valid = [x for x in passports if x.is_valid()]
print(f"There are {len(valid)} valid passports.")