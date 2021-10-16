from loguru import logger


lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]
print(len(lines))

test_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


"""
If I'm understanding this right, there are just three commands...
nop - does nothing
acc - adds (or subtracts) from the accumulator
jmp - jumps to an instruction

- the moment the program tries to run an instruction a second time, you know it
will never terminate.
so..

track whether or not lines have been executed...
Break immeidately on re-execution and display the accumulator.

For teh sample data, we should get "5"
"""

def testlines(lines):
    acc = 0
    execution = 0
    executed = set()
    while execution < len(lines):
        if execution in executed:
            print(f"Re-executing: {execution} - Infinite loop break condition hit.")
            return False
        #print(f"Executing {lines[execution]}")
        executed.add(execution)
        command, value = lines[execution].split()
        value = int(value)
        if command == 'jmp':
            execution += value
        else:
            execution += 1
        if command == 'acc':
            acc += value
        elif command == 'nop':
            pass
    return f"Accumulator is {acc}"

original_lines = lines

for x in range(len(original_lines)):
    logger.debug(f"Permutation {x}")
    newlines = original_lines.copy()
    # try replacing the line at _x_ with jmp if it's a nop, or nop if its jmp.
    # then run the program again, and see if it terminates.
    # if it's not a nop or jmp, then just move to the next line.
    line = newlines[x]
    if line.startswith('nop'):
        line = 'jmp' + line[3:]    
    elif line.startswith('jmp'):
        line = 'nop' + line[3:]
    else:
        continue
    newlines[x] = line
    result = testlines(newlines)
    if result:
        print(result)
        break
