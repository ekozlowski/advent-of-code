from loguru import logger
#lines = open('out.txt', 'r').readlines()
lines = open('input.txt', 'r').readlines()

notes = """
Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or 
aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even 
aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
"""

nice = {
    "qjhvhtzxzqqjkmpb": True,
    "xxyxx": True,
    "uurcxstgmygtbstg": False,
    "ieodomkazucvgmuy": False
}


class SantaString:
    def __init__(self, s):
        self.s = s.strip()
        self.nop = ""
        self.olr = ""
        self.contains_non_overlapping_pair()
        self.one_letter_repeat()

    def __str__(self):
        if self.is_nice():
            nice = 'nice'
        else:
            nice = "naughty"
        return f"<SantaString '{self.s}' is {nice} NOP: {self.nop}, OLR: {self.olr}"

    def contains_non_overlapping_pair(self):
        logger.debug(f"Begin testing string: {self.s}")
        index = 0
        pairs = []
        while index <= len(self.s):
            begin, end = index, index + 2
            test_pair = self.s[begin:end]
            if len(test_pair.strip()) < 2:
                break
            testing_string = self.s[end:]
            logger.debug(f"testing: {self.s[end:]} for pattern {test_pair}")
            if test_pair in testing_string:
                logger.debug(f"Non-Overlapping Pair -> {test_pair}")
                pairs.append(test_pair)
            index += 1
        pairs = list(set(pairs))
        if len(pairs) > 1:
            self.nop = pairs[0]
            #logger.debug("Naughty, because _more than one overlap_")
        elif len(pairs) == 1:
            self.nop = pairs[0]
        else:
            self.nop = ''


    def one_letter_repeat(self):
        for i, c in enumerate(self.s):
            if self.s[i+2:i+3] == c:
                self.olr = self.s[i:i+3]
                return

    def is_nice(self):
        return self.olr and self.nop


if __name__ == "__main__":
#    o = SantaString("wztjkoipxsikoimv")
    nice = []
    naughty = []
    for line in lines:
        o = SantaString(line)
        if o.is_nice():
            nice.append(o)
        else:
            naughty.append(o)

    for o in naughty:
        print(o)

    for o in nice:
        print(o)

    print(len(nice), "Nice SantaStrings")