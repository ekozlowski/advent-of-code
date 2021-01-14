from os import walk
import re

lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]



bags = {}

class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = {}

    def contain(self, name, amount):
        bags[name] = Bag(name)
        self.contains[name] = amount


example_data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

for line in [x for x in example_data.split('\n') if x.strip()]:
    pieces = line.split('bag')
    print('---')
    print(pieces)
    print('---')
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

print(bags)
for b in bags:
    print(bags.get(b).name)
    print(bags.get(b).contains)