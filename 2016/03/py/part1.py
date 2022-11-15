lines = open('../input.txt', 'r').readlines()

count = 0
for l in lines:
    a, b, c = sorted(map(int, l.strip().split()))
    #print(a, b, c)
    if a + b > c:
        count += 1
print(f"There are {count} triangles possible.")