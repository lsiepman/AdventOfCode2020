import re

# DATA
data = []
with open("Data - Day08.txt") as file:
    for line in file:
        data.append(line.strip())

# GOAL 1
"""
Each instruction consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
- acc increases or decreases a single global value called the accumulator by the value given in the argument.
After an acc instruction, the instruction immediately below it is executed next.
- jmp jumps to a new instruction relative to itself. 
The next instruction to execute is found using the argument as an offset from the jmp instruction;
- nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
"""
def acc(instruction, curr_acc):
    num = re.search(r"[0-9-+]+", instruction).group()
    curr_acc += int(num)

    return curr_acc

def jmp(instruction, curr_idx):
    num = re.search(r"[0-9-+]+", instruction).group()
    new_idx = int(num) + curr_idx
    return new_idx

def part1(data):
    accumulator = 0
    i = 0
    seen = {0}
    while True:
        if "acc" in data[i]:
            accumulator = acc(data[i], accumulator)
            i += 1
        elif "jmp" in data[i]:
            i = jmp(data[i], i)
        else:
            i += 1

        old = len(seen)
        seen.add(i)
        if len(seen) == old:
            return accumulator

print(f"The accumulator will reach {part1(data)}")

# GOAL 2
"""
Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). 
What is the value of the accumulator after the program terminates?
"""        
def part2(data):
    nop_locs = [data.index(i) for i in data if "nop" in i]
    jmp_locs = [data.index(i) for i in data if "jmp" in i]

    for n in nop_locs:
        temp = data.copy()
        temp[n] = temp[n].replace("nop", "jmp")

        accumulator = 0
        i = 0
        seen = {0}
        while True: 
            if "acc" in temp[i]:
                accumulator = acc(temp[i], accumulator)
                i += 1
            elif "jmp" in temp[i]:
                i = jmp(temp[i], i)
            else:
                i += 1

            old = len(seen)
            seen.add(i)
            if len(seen) == old:
                break

            if i == len(temp):
                return accumulator

    for n in jmp_locs:
        temp = data.copy()
        temp[n] = temp[n].replace("jmp", "nop")

        accumulator = 0
        i = 0
        seen = {0}
        while True: 
            if "acc" in temp[i]:
                accumulator = acc(temp[i], accumulator)
                i += 1
            elif "jmp" in temp[i]:
                i = jmp(temp[i], i)
            else:
                i += 1

            old = len(seen)
            seen.add(i)
            if len(seen) == old:
                break

            if i == len(temp):
                return accumulator
             
print(f"Now the loop exits at an accumulator value of {part2(data)}")