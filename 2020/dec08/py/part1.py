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

#lines = [x.strip() for x in test_data.split('\n')]
#print(lines)

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

acc = 0
execution = 0
executed = set()
while True:
    if execution in executed:
        print(f"Re-executing: {execution} - break condition hit.")
        break
    print(f"Executing {lines[execution]}")
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
    
print(f"Accumulator is {acc}")