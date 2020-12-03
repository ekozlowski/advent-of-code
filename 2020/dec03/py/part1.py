lines = open('../input.txt', 'r').readlines()
lines = [x.strip() for x in lines]
from itertools import cycle
position = 1
trees = 0
for l in lines:
    moves = 0
    s = ""
    for c in cycle(l):
        moves += 1
        s += c
        if moves == position:
            if c == '#':
                trees += 1
            break
    print(s)
    position += 3
print(f"we hit {trees} trees")
