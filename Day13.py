from functools import reduce
from operator import mul
from sympy import mod_inverse

# INPUT
time_to_arrive = 1000340
lines = "13,x,x,x,x,x,x,37,x,x,x,x,x,401,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,29,x,613,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41"

# GOAL 1
"""What is the ID of the earliest bus you can take to the airport 
multiplied by the number of minutes you'll need to wait for that bus?"""
bus_lines = []
idx = []
for i in lines.split(","):
    try:
        bus_lines.append(int(i))
        idx.append(lines.split(",").index(i))
    except:
        continue

def find_earliest_bus(bus_lines, time_to_arrive):
    min_time = max(bus_lines)
    for i in bus_lines:
        wait = i - (time_to_arrive % i)
        if wait < min_time:
            min_time = wait
            bus = i 
    
    return bus * min_time, bus

print(f"Answer part 1: {find_earliest_bus(bus_lines, time_to_arrive)[0]}, bus {find_earliest_bus(bus_lines, time_to_arrive)[1]}")

# GOAL 2
"""
The shuttle company is running a contest: 
one gold coin for anyone that can find the earliest timestamp such that the first
bus ID departs at that time and each subsequent listed bus ID departs at that subsequent minute. 

An x in the schedule means there are no constraints on what bus IDs must depart at that time.
What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
"""
# chinese remainder theorem applies
def prod(iterable): # default function in the math module in python 3.9
    return reduce(mul, iterable, 1)

def part2(bus_lines, indices):
    N = prod(bus_lines)
    total = []
    for bus, idx in zip(bus_lines, indices):
        total.append(idx * (N // bus) * mod_inverse(N // bus, bus))

    x = sum(total)
    return N - x % N

print(f"At t={part2(bus_lines, idx)} the magical moment will occur")