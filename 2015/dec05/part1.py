from loguru import logger
lines = open('input.txt', 'r').readlines()
vowels = set('aeiou')


def get_vowel_count(s):
    c = 0
    for v in vowels:
        c += s.count(v)
    return c

def has_repeats(s):
    for c in s:
        if f"{c}{c}" in s:
            return True
    return False


def contains_bad_strings(s):
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    for b in bad_strings:
        if b in s:
            return True
    return False


def is_nice(s):
    if get_vowel_count(s) < 3:
        logger.debug("Contained < 3 vowels")
        return False
    if not has_repeats(s):
        logger.debug("Doesn't have repeats")
        return False
    if contains_bad_strings(s):
        logger.debug("Contains bad strings")
        return False
    return True


if __name__ == "__main__":
    nice_count = 0
    for line in lines:
        line = line.strip()
        if is_nice(line):
            logger.debug(f"Line {line} is nice")
            nice_count += 1
        else:
            logger.debug(f"Line {line} is naughty")
    print(f"{nice_count} strings are nice")


