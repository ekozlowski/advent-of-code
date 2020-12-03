"""
I had an epiphany while working the December 3, 2020 puzzle that got me thinking
about modulus and array indexes, and how they work together to essentially 
create an "infinite" index both directions.  (If you wanted your iterable to
repeat, that is, and not throw a IndexError exception.)

For example, with the string s='abc', requesting index 0 returns 'a', while
ordinairly requesting index 3 raises IndexError.

If we change that instead to reqeust [3 % len(s)], we get back 'a', and we can
keep increasing the requested index, infinitely repeating the iterable.

In the case of s='abc',Requesting [-1 % len(s)] results in 'c' being returned,
which means our iterable is in effect, infinitely repeating, both directions.
"""

def modrepeat(iterable, index):
    return iterable[index % len(iterable)]

s = 'abc'

# forwarwd
print("Forward")
for x in range(5):
    print(x, modrepeat(s, x))

# backward
print("Backward")
for x in range(0, -5, -1):
    print(x, modrepeat(s, x))