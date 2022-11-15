data = open('../input.txt', 'r').read()
print(len(data))

class Heading:
    def __init__(self):
        self.heading = "N"

    def turn(self, direction):
        if direction == "L":
            if self.heading == "N":
                self.heading = "W"
            elif self.heading == "W":
                self.heading = "S"
            elif self.heading == "S":
                self.heading = "E"
            elif self.heading == "E":
                self.heading = "N"
            else:
                raise Exception(f"self.heading is impossible for turning. {self.heading}")
        elif direction == "R":
            if self.heading == "N":
                self.heading = "E"
            elif self.heading == "E":
                self.heading = "S"
            elif self.heading == "S":
                self.heading = "W"
            elif self.heading == "W":
                self.heading = "N"
            else:
                raise Exception(f"self.heading is impossible for turning. {self.heading}")
        else:
            raise Exception(f"direction '{direction}' invalid - should be 'L' or 'R'")

class Player:
    def __init__(self):
        self.position = [0, 0]  # (x, y)
        self.heading = Heading()
        self.visited_coords = []

    def move(self, vector):
        # vector is <turn><spaces>
        # where you turn L|R, and move <spaces> in that direction.
        self.heading.turn(vector[0])
        spaces = int(vector[1:])
        while spaces > 0:
            if self.heading.heading == "N":  # add to Y
                res = self.position[1]
                res += 1
                self.position[1] = res
            elif self.heading.heading == "E": # add to X
                res = self.position[0]
                res += 1
                self.position[0] = res
            elif self.heading.heading == "S": # subtract from Y
                res = self.position[1]
                res -= 1
                self.position[1] = res
            elif self.heading.heading == "W": # subtract from X
                res = self.position[0]
                res -= 1
                self.position[0] = res
            else:
                Exception("Can't move that direction")
            t = tuple(self.position)
            if t not in self.visited_coords:
                self.visited_coords.append(t)
            else:
                print(f"visited again! -> {t}")
                print(f"Distance: {self.get_distance()}")
            spaces = spaces - 1
    def get_distance(self):
        return abs(self.position[0]) + abs(self.position[1])

p = Player()
p.move('R2')
p.move('L3')
print(p.position)
print(p.get_distance())
p = Player()
p.move('R2')
p.move('R2')
p.move('R2')
print(p.position)
print(p.get_distance())

p = Player()
vectors = data.split(',')
for v in [x.strip() for x in vectors]:
    p.move(v)
print(p.get_distance())
print(p.position)