data = open('../input.txt', 'r').read()

present_grid = {}

class Santa:
    def __init__(self, present_grid):
        self.present_grid = present_grid
        self.x_pos = 0
        self.y_pos = 0

    def deliver(self):
        key = (self.x_pos, self.y_pos)
        value = self.present_grid.setdefault(key, 0)
        value += 1
        self.present_grid[key] = value

    def move(self, direction):
        if direction == "^":
            self.y_pos += 1
        elif direction == "v":
            self.y_pos -= 1
        elif direction == ">":
            self.x_pos += 1
        elif direction == "<":
            self.x_pos -= 1
        else:
            raise Exception(f"Unknown direction {direction}")
        # right after we move, we deliver a present...
        self.deliver()


if __name__ == "__main__":
    santa = Santa(present_grid)
    robosanta = Santa(present_grid)

    santa.deliver()
    robosanta.deliver()
    for i, c in enumerate(data):
        if i % 2 == 0:
            santa.move(c)
        else:
            robosanta.move(c)
    print(len(present_grid))
