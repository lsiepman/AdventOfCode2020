import re
from itertools import combinations_with_replacement, permutations

# DATA
data = []
with open("Data - Day14.txt") as file:
    for line in file:
        data.append(line.strip())

# create dict with memory adresses
memory = {}
for line in data:
    if "mem" in line:
        memory[int(re.search(r"mem\[([0-9]+)\]", line).group(1))] = [0]*36

# GOAL 1
"""
The initialization program (your puzzle input) can either update the bitmask or write a value to memory. 
Values and memory addresses are both 36-bit unsigned integers. 

The bitmask is always given as a string of 36 bits, written with the most significant bit (representing 2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged.
To initialize your ferry's docking program, you need the sum of all values left in memory after the initialization program completes. 
(The entire 36-bit address space begins initialized to the value 0 at every address.)

Execute the initialization program. What is the sum of all values left in memory after it completes?
"""
def process_mask(mask, value):
    new = []
    for i,j in zip(mask, value):
        if i == "X":
            new.append(j)
        else:
            new.append(i)

    return new

def convert_to_list(line):
    if "mask" in line:
        return list(re.search(r"mask = ([X0-9]+)", line).group(1))
    
    value = re.search(r"mem\[[0-9]+\] = ([0-9]+)", line).group(1)
    value = str(bin(int(value)))[2:]
    return f"{value:0>36}"

def find_address(line):
    return int(re.search(r"mem\[([0-9]+)\]", line).group(1))

def convert_to_ints(memory):
    result = []
    for i in memory:
        string = "".join(memory[i])
        result.append(int(string, 2))
    
    return result

def part1(data, memory):
    mask = ["X"]*36
    for line in data:
        if "mask" in line:
            mask = convert_to_list(line)
        else:
            address = find_address(line)
            inp = convert_to_list(line)
            conv = process_mask(mask, inp)
            memory[address] = conv

    return sum(convert_to_ints(memory))

print(f"The sum of all values equals {part1(data, memory)}")

# GOAL 2
"""
A version 2 decoder chip doesn't modify the values being written at all. 
Instead, it acts as a memory address decoder. 
Immediately before a value is written to memory, 
each bit in the bitmask modifies the corresponding bit of the destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.

A floating bit is not connected to anything and instead fluctuates unpredictably. 
In practice, this means the floating bits will take on all possible values, 
potentially causing many memory addresses to be written all at once!
"""
def find_address_part2(line, mask):
    int_val = find_address(line)
    bin_val = str(bin(int(int_val)))[2:]
    general_address = list(f"{bin_val:0>36}")

    new = []
    for i,j in zip(mask, general_address):
        if i == "0":
            new.append(j)
        elif i == "1":
            new.append(i)
        elif i == "X":
            new.append(i)

    indices = [i for i, x in enumerate(new) if x == "X"]
    combi = list(combinations_with_replacement(["0", "1"], len(indices)))
    ordered_combi = []
    for i in combi:
        perm = set(permutations(i))
        for j in perm:
            ordered_combi.append(list(j))

    mem_addresses = []
    for x in list(ordered_combi):
        temp = []
        for i in new:
            if i == "X":
                temp.append(x.pop())
            else: 
                temp.append(i)
        
        mem_addresses.append("".join(temp))
    
    return mem_addresses

def find_and_add_value(mem_addresses, line, memory):
    value = int(re.search(r"mem\[[0-9]+\] = ([0-9]+)", line).group(1))

    for i in mem_addresses:
        memory[i] = value


def part2(data):
    memory = {}
    mask = ["0"] * 36

    for line in data:
        if "mask" in line:
            mask = convert_to_list(line)
        else:
            mem_ads = find_address_part2(line, mask)
            find_and_add_value(mem_ads, line, memory)

    return sum(list(memory.values()))

print(f"In version 2 of the program, the sum equals {part2(data)}")


