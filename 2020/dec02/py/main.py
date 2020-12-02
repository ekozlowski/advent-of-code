data = open("../input.txt", 'r').readlines()

def solve_first_half():
    print(f"Total passwords: {len(data)}")
    invalid = []
    valid = []
    for d in data:
        policy, password = [x.strip() for x in d.split(':')]
        repeats, letter = [x.strip() for x in policy.split()]
        repeat_begin, repeat_end = map(int, repeats.split('-'))
        count = password.count(letter)
        if count >= repeat_begin and count <= repeat_end:
            valid.append(d)
        else:
            invalid.append(d)
    print(f"Count of Valid Passwords: {len(valid)}")
    print(f"Count of Invalid Passwords: {len(invalid)}")


def solve_second_half():
    print(f"Total passwords: {len(data)}")
    invalid = []
    valid = []
    for d in data:
        policy, password = [x.strip() for x in d.split(':')]
        positions, letter = [x.strip() for x in policy.split()]
        first_pos, second_pos = map(int, positions.split('-'))
        if password[first_pos-1] == letter:
            if password[second_pos-1] != letter:
                valid.append(d)
            else:
                invalid.append(d)
        elif password[second_pos-1] == letter:
            valid.append(d)
        else:
            invalid.append(d)
    print(f"Count of Valid Passwords: {len(valid)}")
    print(f"Count of Invalid Passwords: {len(invalid)}")


if __name__ == "__main__":
    print("--- First Half solution ---")
    solve_first_half()
    print("--- Second Half Solution ---")
    solve_second_half()
