lines = open('../input.txt', 'r').readlines()
lines = [x.strip() for x in lines]
from itertools import cycle
def get_trees(right_dim, down_dim):
    position = 1
    trees = 0
    for i, l in enumerate(lines):
        if i % down_dim != 0:
            continue
        moves = 0
        s = ""
        for c in cycle(l):
            moves += 1
            s += c
            if moves == position:
                if c == '#':
                    trees += 1
                break
        #print(s)
        position += right_dim
    print(f"we hit {trees} trees with right {right_dim} and down {down_dim}")
    return trees
t1 = get_trees(1, 1)
t2 = get_trees(3, 1)
t3 = get_trees(5, 1)
t4 = get_trees(7, 1)
t5 = get_trees(1, 2)
print(f"Multiplied: {t1 * t2 * t3 * t4 * t5}")