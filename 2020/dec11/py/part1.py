data = open('../input.txt', 'r').readlines()
newdata = []

def get_pos(x, negy):
    if negy < 0:
        return None
    if x < 0:
        return None
    if x > len(data[0])-1:
        return None
    if negy > len(data)-1:
        return None
    return data[negy][x]

        
for negy, line in enumerate(data):
    for x, char in enumerate(line):
        print(f"negy: {negy} x {x} {get_pos(x, negy)}")

