from os import walk
import re

lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]

bags = {}

for line in lines:
    bag, *contains = re.findall(r'(\w+ \w+) bags?', line)
    b = bags.setdefault(bag, {})
    for c in contains:
        b.setdefault('contains', set()).add(c)

        inner = bags.setdefault(c, {})
        inner.setdefault('is_contained_by', set()).add(bag)
        

sg = bags['shiny gold']

bags_that_contain = set()
def walk_back_up_the_tree(initial_bag):
    bag = initial_bag
    
    is_contained_by = bags.get(bag).get('is_contained_by')
    if is_contained_by:
        for b in is_contained_by:
            bags_that_contain.add(b)
            walk_back_up_the_tree(b)

walk_back_up_the_tree('shiny gold')
print(len(bags_that_contain), "bags can be an outer container for a shiny gold bag")
