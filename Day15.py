# DATA
data = [6, 13, 1, 15, 2, 0]

# GOAL 1
"""
In this game, the players take turns saying numbers. 
They begin by taking turns reading from a list of starting numbers (your puzzle input). 
Then, each turn consists of considering the most recently spoken number:

    If that was the first time the number has been spoken, the current player says 0.
    Otherwise, the number had been spoken before; the current player announces how many 
    turns apart the number is from when it was previously spoken.

So, after the starting numbers, each turn results in that player speaking aloud either 0 
(if the last number is new) or an age (if the last number is a repeat).

Given your starting numbers, what will be the 2020th number spoken?
"""
def get_diff_index(item, lst):
    indices = [i for i, x in enumerate(lst) if x == item]
    return indices[-1] - indices[-2]

def part1(inp, max_val):
    while len(inp) < max_val:
        val = inp[-1]
        if val in inp[:-1]:
            diff = get_diff_index(val, inp)
            inp.append(diff)
        else:
            inp.append(0)
    
    return inp[max_val-1]

print(f"{part1(data.copy(), 2020)} will be the 2020th number spoken")

# GOAL 2
"""
Given your starting numbers, what will be the 30000000th number spoken?
"""
def part2(inp, max_val):
    indices = {}
    for i, j in enumerate(inp):
        indices[j] = i + 1

    x = len(inp)
    val = inp[-1]

    while x < max_val:   
        if indices.get(val):
            prev = indices[val]
            indices[val] = x
            val = x - prev
        else:
            indices[val] = x 
            val = 0
        x += 1

    return val

print(f"{part2(data, 30000000)} will be the 30000000th number spoken")
part2(data, 30000000)



