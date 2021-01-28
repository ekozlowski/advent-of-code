from itertools import combinations
from functools import reduce

sample = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

#sample_ints = map(int, sample.split('\n'))
#sample_ints = list(sample_ints)

weakness_int = 1639024365

ints = list(map(int, open('../input.txt', 'r').readlines()))

def get_valid_values():
    # any values <= the weakness_int won't sum to it, so we can disqualify those
    valid_values = [x for x in ints if x < weakness_int]
    return valid_values

# start at the first value, and work to the end, when we hit the sum, return 
# where we started and ended.
start = 0
index = 0
found = False
valid_values = get_valid_values()
while not found:
    start = index
    this_sum = sum(valid_values[start:index])
    if this_sum > weakness_int:
        start += 1
        print(valid_values[start:index])
    elif 
    else:
        index += 1
    
print(f"Start {start}, End: {index}")
print(f"{valid_values[start: start+index]}")
