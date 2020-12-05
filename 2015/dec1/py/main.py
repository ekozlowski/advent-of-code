value_map = {")": -1, "(": 1}
data = [value_map.get(d) for d in list(open("../input.txt", "r").read().strip())]

def solve_part_1():
    print(sum([value_map.get(d) for d in data]))


def solve_part_2():
    for i, e in enumerate(data):
        if sum(data[0:i]) == -1:
            print(i)
            break


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()
