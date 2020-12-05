lines = open("../input.txt", "r").readlines()


def between(begin, end):
    # return a function that takes one argument, and determines if it is
    # between (inclusive) the two values passed in.
    def f(x):
        return begin <= int(x) <= end

    return f


def endswith(ending_list):
    def f(x):
        for ending in ending_list:
            if x.endswith(ending):
                return True
        return False

    return f


def endswithbetween(units, begin, end):
    def f(x):
        if units and x.endswith(units):
            x = x.replace(units, "")
            return begin <= int(x) <= end
        # if the predicate doesn't match, we don't care, it's still "valid"
        # as far as we're cocerned...
        return True

    return f


def memberof(elements):
    def f(x):
        return x in elements

    return f


def length(some_length):
    def f(x):
        return len(x) == some_length

    return f


def numeric():
    def f(x):
        return x.isnumeric()

    return f


def startswith(char):
    def f(x):
        return x.startswith(char)

    return f


def chars_after_first_in(chars):
    def f(x):
        for c in x[1:]:  # skip the first character - it's #.
            if c not in chars:
                return False
        return True

    return f


class Passport:
    def __init__(self, data):
        self.data = data
        self.fields = self.parse()
        self.valid = True
        self.validators = {
            "byr": [between(1920, 2002)],
            "iyr": [between(2010, 2020)],
            "eyr": [between(2020, 2030)],
            "hgt": [
                endswith(["cm", "in"]),
                endswithbetween("cm", 150, 193),
                endswithbetween("in", 59, 76),
            ],
            "hcl": [startswith("#"), chars_after_first_in("#abcdefg0123456789")],
            "ecl": [memberof(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])],
            "pid": [length(9), numeric()],
        }

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
        fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for r in required:
            if r not in self.fields:
                return False
        valid = True
        for v in self.validators:
            validator_methods = self.validators.get(v)
            field_value = self.fields.get(v)
            for method in validator_methods:
                if method(field_value) == False:
                    valid = False
                    break
        return valid


def get_passports():
    """
    Chunks the "file" into lists of lines representing individual passport
    data.
    """
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


if __name__ == "__main__":
    valid = [x for x in get_passports() if x.is_valid()]
    print(f"There are {len(valid)} valid passports.")
