ints = [int(x) for x in open('../input.txt', 'r').readlines()]

ints.sort()
print(ints)

ones = 0
twos = 0
threes = 0

for i, x in enumerate(ints):
    if i == 0:
        initial = 0
    else:
        initial = ints[i-1]
    total = x - initial
    if total == 1:
        ones += 1
    elif total == 2:
        twos += 1
    elif total == 3:
        threes += 1
    else:
        raise Exception(f"Difference {total} not found")
# our regular adapter
threes += 1
# zero -> initial

print(f"Ones: {ones} Twos: {twos} Threes {threes}")
print(f"ones {ones} times threes {threes} is {ones*threes}")