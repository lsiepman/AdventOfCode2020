

# DATA
data = []
with open("Data - Day09.txt") as file:
    for line in file:
        data.append(int(line.strip()))

# GOAL 1
"""
Find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. 
What is the first number that does not have this property?
"""

def check_value(curr_val, past_vals):
    for val1 in past_vals:
        for val2 in past_vals:
            if val1 + val2 == curr_val:
                return True
    
    return False

def select_past(data, curr_idx, len_past):
    low_idx = curr_idx - len_past
    return data[low_idx:curr_idx]

def part1(data, len_past):
    i = len_past
    while True:
        past = select_past(data, i, len_past)
        if not check_value(data[i], past):
            return data[i]
        else:
            i += 1

ans1 = part1(data, 25) 
print(f"{ans1} does not comply with the rules")

# GOAL 2
"""
Find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
To find the encryption weakness, add together the smallest and largest number in this contiguous range;
What is the encryption weakness in your XMAS-encrypted list of numbers?
"""
def find_contiguous(data, goal):
    j = 0
    while True:
        temp = 0
        vals = []
        i = j
        while temp < goal:
            temp += data[i]
            vals.append(data[i])
            i += 1

            if temp == goal:
                return vals
        
        j += 1

def part2(data, goal):
    contiguous = find_contiguous(data, goal)
    return min(contiguous) + max(contiguous)

print(f"The encryption weakness equals {part2(data, ans1)}")
        


