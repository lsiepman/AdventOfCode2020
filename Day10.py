from itertools import combinations

data = [0]
with open("Data - Day10.txt") as file:
    for line in file:
        data.append(int(line.strip()))
data = sorted(data)
data.append(max(data) + 3)

# GOAL 1
"""What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?"""

# ANSWER 1
def find_diff(data):
    return [x - data[i - 1] for i, x in enumerate(data)][1:]

def part1(data):
    diffs = find_diff(data)
    cnt1 = 0
    cnt3 = 0
    for i in diffs:
        if i == 1:
            cnt1 += 1
        elif i == 3:
            cnt3 += 1

    return cnt1 * cnt3

print(f"The first answer equals {part1(data)}")

# GOAL 2
"""What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?"""

def find_paths(subset):
    if len(subset) == 0 or len(subset) == 1:
        return 1
    start = subset.pop(0)
    end = subset.pop(-1)

    combs = []
    for i in range(1, len(subset) + 1):
        temp = list(combinations(subset, i))
        combs.extend(temp)

    options = []
    for i in combs:
        new = [start] + list(i) + [end]
        diffs = find_diff(new)
        if all(0 < x < 4 for x in diffs):
            options.append(new)

    if end - start <= 3:
        options.append([start] + [end])

    if len(options) > 0:
        return len(options)
    else:
        return 1

def part2(data):
    start = 0
    prev = 0
    paths = 1
    for idx, val in enumerate(data):
        if prev + 3 == val:
            paths_here = find_paths(data[start:idx])
            paths *= paths_here
            start = idx
        prev = val

    return paths
        
print(f"There are {part2(data)} combinations of adapters")