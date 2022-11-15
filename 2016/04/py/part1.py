from collections import Counter
rooms_data = open('../input.txt', 'r').readlines()

class Room:
    def __init__(self, data):
        self.data = data
        self.encrypted = ''.join(data.split('-')[:-1])
        self.encrypted = ''.join(sorted(self.encrypted))
        self.sector_id = int(data.split("[")[0].split('-')[-1])
        self.checksum = data.split("[")[-1].split("]")[0]

    @property
    def real(self):
        c = Counter(self.encrypted)
        return ''.join([x[0] for x in c.most_common(5)]) == self.checksum


rooms = [Room(r) for r in rooms_data]
real_rooms = [r for r in rooms if r.real]

print(f"There are {len(real_rooms)} real rooms.")
print(f"Their sums of sector IDs are: {sum([x.sector_id for x in real_rooms])}")