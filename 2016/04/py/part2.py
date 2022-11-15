from collections import Counter
from itertools import cycle
rooms_data = open('../input.txt', 'r').readlines()

letters = cycle(['abcdefghijklmnopqrstuvwxyz'])

class Room:
    def __init__(self, data):
        self.data = data
        self.encrypted = ''.join(data.split('-')[:-1])
        self.sector_id = int(data.split("[")[0].split('-')[-1])
        # sector id mod 26 is how much letters are "shifted"
        self.letter_shift = self.sector_id % 26
        for c in self.encrypted:
            pass

    @property
    def real(self):
        c = Counter(self.encrypted)
        #return ''.join([x[0] for x in c.most_common(5)]) == self.checksum

    def decrypt(self):
        n = self.sector_id
        from string import ascii_lowercase as lc
        n = n % len(lc)
        lookup = str.maketrans(lc, lc[n:] + lc[:n])
        return self.encrypted.translate(lookup)

rooms = [Room(r) for r in rooms_data]

for r in rooms:
    print(r.sector_id, r.decrypt())