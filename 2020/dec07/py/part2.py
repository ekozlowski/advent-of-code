from os import walk
lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]

bags = {}

class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = []

    def __str__(self):
        return f"<Bag: {self.name}>"

    def __repr__(self):
        return str(self)

    def contain(self, name, amount):
        # I am deliberately flatting the objects here, and storing one _per_
        # count, in order to make the calculation of how many are contained
        # within easier to use recursion on.
        for _ in range(amount):
            b = bags.setdefault(name, Bag(name))
            self.contains.append(b)


example_data = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

for line in lines: # [x for x in example_data.split('\n') if x.strip]:
    pieces = line.split('bag')
    this_bag = pieces[0].strip()
    this_bag = bags.setdefault(this_bag, Bag(this_bag))
    for p in pieces[1:]:
        if p.strip() == '.':
            continue
        if p.startswith('s contain'):
            p = ''.join(p[10:])
        if p.startswith('s, '):
            p = ''.join(p[3:])
        if p.startswith(', '):
            p = ''.join(p[2:])
        if p == 'no other ' or p == 's.':
            continue
        try:
            number, a, b = p.split()
            number = int(number)
            this_bag.contain(' '.join([a, b]), number)
        except:
            print(p)
            raise

bag = bags.get('shiny gold')

count = 0

def get_count(bag):
    global count
    count += len(bag.contains)
    for bag in bag.contains:
        get_count(bag)

get_count(bags.get('shiny gold'))
print(f"A 'shiny gold' bag contains {count} other bags.")

