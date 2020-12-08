lines = open("../input.txt", 'r').readlines()

class PeopleGroup:
    def __init__(self, lines):
        self.lines = lines
    
    def get_unique_character_count(self):
        data = "".join(self.lines)
        data = data.replace('\n', '')
        print(data)
        return len(list(set(data)))

def get_peoplegroups():
    groups = []
    g = []
    for l in lines:
        if not l.strip() and g:
            groups.append(PeopleGroup(g))
            g = []
        else:
            g.append(l)
    if g:
        groups.append(PeopleGroup(g))
    return groups

if __name__ == "__main__":
    print(sum([x.get_unique_character_count() for x in get_peoplegroups()]))