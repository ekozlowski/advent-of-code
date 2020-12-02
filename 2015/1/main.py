def solve_part_1():
    data = open("input.txt", 'r').read()
    floor = 0
    character = 0
    for d in data:
        if d == ")":
            floor -= 1
        if d == "(":
            floor += 1
    print(f"Part 1 solution: {floor}")


def solve_part_2():
    data = open("input.txt", 'r').read()
    floor = 0
    character_position = 0
    for d in data:
        if d == ")":
            floor -= 1
        if d == "(":
            floor += 1
        character_position += 1
        if floor < 0:
            break
    print(f"Part 2 solution: {character_position}")

if __name__ == "__main__":
    solve_part_1()
    solve_part_2()