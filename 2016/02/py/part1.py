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

codes = []

posmap = {
    (-1, 1): "1",
    (0, 1): "2",
    (1, 1): "3",
    (-1, 0): "4",
    (0, 0): "5",
    (1, 0): "6",
    (-1, -1): "7",
    (0, -1): "8",
    (1, -1): "9"
}

for l in lines:
    pos = [0, 0]
    for c in l.strip():
        move = coord_map.get(c)
        pos[0] += move[0]
        pos[1] += move[1]
        if pos[0] < -1:
            pos[0] = -1
        if pos[0] > 1:
            pos[0] = 1
        if pos[1] < -1:
            pos[1] = -1
        if pos[1] > 1:
            pos[1] = 1
    print(pos)
    print(posmap.get(tuple(pos)))

# Code looks like:
#[0, -1] 7
#[0, 1] 6
#[1, -1] 8
#[0, 0] 5
#[0, -1] 7