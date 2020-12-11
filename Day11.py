from copy import deepcopy

# DATA
data = []
with open("Data - Day11.txt") as file:
    for line in file:
        row = []
        for char in line.strip():
            row.append(char)
        data.append(row)

# GOAL 1
"""
By modeling the process people use to choose (or abandon) their seat in the waiting area, 
you're pretty sure you can predict the best place to sit. 
You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. 
Each position is either floor (.), an empty seat (L), or an occupied seat (#).

All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.

Floor (.) never changes; seats don't move, and nobody sits on the floor.
"""                    
def find_neighbours(data, x, y, occ=True):
    neighbours = [(-1, -1), (-1, 0), (-1, 1), 
                  (0,-1), (0, 1), 
                  (1, -1), (1, 0), (1, 1)]

    cnt = 0
    for i, j in neighbours:
        if x-i in range(len(data)) and y-j in range(len(data[0])) and data[x-i][y-j] == "#":
            cnt += 1

    if occ:
        if cnt < 4:
            return "#"
        else:
            return "L"
    else:
        if cnt > 0:
            return "L"
        else: 
            return "#"

def count_occupied(data):
    cnt = 0
    for i in data:
        cnt += i.count("#")

    return cnt


def part1(data):
    while True:
        new = []
        for i in range(len(data)):
            row = []
            for j in range(len(data[0])):
                if data[i][j] == ".":
                    row.append(".")
                elif data[i][j] == "#":
                    row.append(find_neighbours(data, i, j))
                else:
                    row.append(find_neighbours(data, i, j, False))
            new.append(row)

        if data == new:
            return count_occupied(data)
        else:
            data = deepcopy(new)
 
print(f"{part1(deepcopy(data))} seats are occupied")

# GOAL 2
"""
People don't just care about adjacent seats - 
they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, 
consider the first seat in each of those eight directions.

Also, people seem to be more tolerant than you expected: 
it now takes five or more visible occupied seats for an occupied seat to become empty 
(rather than four or more from the previous rules).
"""

def seen_chairs(data, x, y, occ=True):
    neighbours = [(-1, -1), (-1, 0), (-1, 1), 
                  (0,-1), (0, 1), 
                  (1, -1), (1, 0), (1, 1)]

    cnt = 0
    for i, j in neighbours:
        free_sightline = True
        dist = 1 # looking distance

        while free_sightline and dist < len(data):
            if x-i*dist in range(len(data)) and y-j*dist in range(len(data[0])) and data[x-i*dist][y-j*dist] == "#":
                cnt += 1
                free_sightline = False
            elif x-i*dist in range(len(data)) and y-j*dist in range(len(data[0])) and data[x-i*dist][y-j*dist] == "L":
                free_sightline = False
            else:
                 dist += 1

    if occ:
        if cnt < 5:
            return "#"
        else:
            return "L"
    else:
        if cnt > 0:
            return "L"
        else: 
            return "#"

def part2(data):
        while True:
            new = []
            for i in range(len(data)):
                row = []
                for j in range(len(data[0])):
                    if data[i][j] == ".":
                        row.append(".")
                    elif data[i][j] == "#":
                        row.append(seen_chairs(data, i, j))
                    else:
                        row.append(seen_chairs(data, i, j, False))
                new.append(row)

            if data == new:
                return count_occupied(data)
            else:
                data = deepcopy(new)
 
print(f"{part2(deepcopy(data))} seats are occupied")







