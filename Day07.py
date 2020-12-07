import re

# DATA
data = []
with open("Data - Day07.txt") as file:
    for line in file:
        data.append(line.strip())

bags = {}
for i in data:
    adj = i.split(" ")[0]
    colour = i.split(" ")[1]
    bags[f"{adj} {colour}"] = i.split(" contain ")[1]

for key in bags:
    string = bags[key]
    nums = re.findall("[0-9]+", string)
    colour = re.findall("[a-z]+ [a-z]+", string)
    bags[key] = {"nums": nums, "colour": colour}

# GOAL 1
"""
Bags must be color-coded and must contain specific quantities of other color-coded bags. 
How many bag colors can eventually contain at least one shiny gold bag?
"""
def find_direct(bags, colour):
    cols = []
    for key in bags:
        if colour in bags[key]["colour"]:
            cols.append(key)
    return cols

def find_indirect(bags, start="shiny gold"):
    seen = {start}
    while True:
        old = len(seen)
        work_lst = []
        for i in seen:
            work_lst.extend(find_direct(bags, i))
        
        seen.update(work_lst)
        if len(seen) == old:
            seen.remove(start)
            return seen

def part1(bags):
    print(f"There are {len(find_indirect(bags))} bags that can contain a shiny gold bag")

part1(bags)

# GOAL 2
"""
How many individual bags are required inside your single shiny gold bag?
"""
def find_inside(bags, colour):
    master_list = []
    nums = bags[colour]["nums"]
    cols = bags[colour]["colour"]
    if "no other" in cols:
        return 

    for i, j in enumerate(nums):
        for x in range(int(j)):
            master_list.append(cols[i])

    return master_list

def part2(bags, colour="shiny gold"):
    result = []
    cols = [colour]
    while True:
        temp = []
        for i in cols:
            inside = find_inside(bags, i)
            if inside is not None:
                temp.extend(inside)
            
        if len(temp) == 0:
            return len(result)
        else:
            cols = temp
            result.extend(temp)
    
print(f"There are {part2(bags)} bags inside the shiny gold bag")
