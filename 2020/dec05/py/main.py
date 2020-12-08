data = [x.strip() for x in open("../input.txt").readlines() if x.strip()]

test_data = """
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""


def bisect(input_list):
    first_half = input_list[: len(input_list) // 2]
    second_half = input_list[len(input_list) // 2 :]
    return first_half, second_half


def _get_list_bisection(input, range_value, lower_indicator, upper_indicator):
    vals = list(range(range_value))
    for c in input:
        if c == lower_indicator:
            vals = bisect(vals)[0]
        elif c == upper_indicator:
            vals = bisect(vals)[1]
        else:
            raise Exception(f"Invalid value for range {c}")
    if len(vals) == 1:
        return vals[0]
    else:
        raise Exception(f"Could not determine column based on input {input}")


def get_row(input):
    return _get_list_bisection(input, 128, "F", "B")


def get_column(input):
    return _get_list_bisection(input, 8, "L", "R")


def get_seat_id(row_input, col_input):
    return ((get_row(row_input) * 8) + get_column(col_input))

def test():
    highest = 0
    seats = []
    for d in data:
        print(f"Input {d}")
        row_input, col_input = d[0:7], d[7:]
        print(f"Row Input: {row_input} Col Input: {col_input}")
        result = get_seat_id(row_input=row_input, col_input=col_input)
        if result > highest:
            highest = result
        seats.append(result)
    print(f"Highest Seat ID: {highest}")
    seats.sort()
    print(seats)
    for x in range(0, 128):
        for y in range(0, 8):
            seat_id = (x * 8) + y
            if seat_id not in seats:
                print(f"Row {x} Col: {y} ID: {(x * 8) + y}")
    
if __name__ == "__main__":
    test()