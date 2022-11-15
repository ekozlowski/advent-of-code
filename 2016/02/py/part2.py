lines = open('../input.txt', 'r').readlines()
print(len(lines))
print(lines)

coord_map = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

# (0, 0) = "5", (1, 1) = "3", (-1, 0) = "4", etc...

posmap = {
    (-2, 0): "5",
    (-1, 1): "2",
    (-1, 0): "6",
    (-1, -1): "A",
    (0, 2): "1",
    (0, 1): "3",
    (0, 0): "7",
    (0, -1): "B",
    (0, -2): "D",
    (1, 0): "8",
    (1, 1): "4",
    (1, -1): "C",
    (2, 0): "9"
}

for l in lines:
    pos = [-2, 0]
    for c in l.strip():
        move = coord_map.get(c)
        if tuple((pos[0] + move[0], pos[1] + move[1])) not in posmap:
            # ignore it,invalid move.
            pass
        else:
            pos[0] = pos[0] + move[0]
            pos[1] = pos[1] + move[1]
        
    print(pos)
    print(posmap.get(tuple(pos)))
