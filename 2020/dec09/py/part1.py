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

ints = list(map(int, open('../input.txt', 'r').readlines()))

def get_valid_values(begin, end):
    valid_values = [x+y for x,y in list(combinations(ints[begin:end], 2))]
    return set(valid_values)
    
for i, x in enumerate(ints[25:]):
    valid_values = get_valid_values(i, 25+i)
    if x not in valid_values:
        print(f"{x} is not in valid values.")