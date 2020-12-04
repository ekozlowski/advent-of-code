from itertools import combinations
from functools import reduce

numbers = list(map(int, open('../data.txt', 'r').readlines()))

def get_2020_product(sequence, length):
    return reduce(lambda a,b: a*b, [x for x in combinations(sequence, length) if sum(x) == 2020][0])

def solve_part_1():
    print(f"Part one solution: {get_2020_product(numbers, 2)}")

def solve_part_2():
    print(f"Part two solution: {get_2020_product(numbers, 3)}")

if __name__ == "__main__":
    solve_part_1()
    solve_part_2()
