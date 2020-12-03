from functools import reduce
import numpy as np

# DATA
data = []
with open("Data - Day03.txt") as file:
    for line in file:
        line_data = []
        for char in line:
            if char == "#" or char == ".":
                line_data.append(char)

        data.append(line_data)

area = np.array(data)

# GOAL 1
"""
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
These aren't the only trees, though; 
due to something you read about once involving arboreal genetics and biome stability, 
the same pattern repeats to the right many times

start by counting all the trees you would encounter for the slope right 3, down 1
starting position at the top-left
"""

def move(grid, cur_y, cur_x, val_y, val_x):
    new_y = cur_y + val_y
    new_x = (cur_x + val_x) % len(grid[0])

    return new_y, new_x

def check_tree(grid, y, x):
    if grid[y][x] == ".":
        return False
    else:
        return True

def part1(grid, y, x):
    trees = []
    while y < len(grid) - 1:
        y, x = move(grid, y, x, 1, 3)
        trees.append(check_tree(grid, y, x))
    
    return sum(trees)


print(f"Answer 3a: {part1(area, 0, 0)}")
# GOAL 2
"""
Determine the number of trees you would encounter if, 
for each of the following slopes, you start at the top-left corner 
and traverse the map all the way to the bottom:
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""
def part2(grid):
    results =[]
    for combination in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        y = 0
        x = 0
        trees = [False]
        while y < len(grid) - 1:
            y, x = move(grid, y, x, combination[0], combination[1])
            trees.append(check_tree(grid, y, x))

        results.append(sum(trees))
    print(results)

    return reduce((lambda x, y: x * y), results)


print(f"Answer 3b: {part2(area)}")


