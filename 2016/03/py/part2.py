lines = open('../input.txt', 'r').readlines()

count = 0
for i, l in enumerate(lines):
    if i % 3 == 0:
        # three triangles, x, y, z:
        x = []
        y = []
        z = []
        pieces = list(map(int, l.strip().split()))
        x.append(pieces[0])
        y.append(pieces[1])
        z.append(pieces[2])
        pieces = list(map(int, lines[i+1].strip().split()))
        x.append(pieces[0])
        y.append(pieces[1])
        z.append(pieces[2])
        pieces = list(map(int, lines[i+2].strip().split()))
        x.append(pieces[0])
        y.append(pieces[1])
        z.append(pieces[2])
        for triangle in [x, y, z]:
            a, b, c = sorted(triangle)
            if a + b > c:
                count += 1
    
print(f"There are {count} triangles possible.")