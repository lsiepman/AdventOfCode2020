# DATA
data = []
with open("Data - Day01.txt") as file:
    for line in file:
        data.append(int(line.strip()))
# GOAL 1
"""
Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

# ANSWER 1
def part1(data):
    for val1 in data:
        for val2 in data:    
            if val1 + val2 == 2020:
                print(f"values are {val1, val2}")
                return val1 * val2

print(f"The first answer of the year is {part1(data)}")

# GOAL 2
"""In your expense report, what is the product of the three entries that sum to 2020?"""

# ANSWER 2
def part2(data):
    for val1 in data:
        for val2 in data:
            for val3 in data:
                if val1 + val2 + val3 == 2020:
                    print(f"values are {val1, val2, val3}")
                    return val1 * val2 * val3
                    
print(f"The second answer of the year is {part2(data)}")