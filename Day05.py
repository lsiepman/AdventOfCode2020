import re

# DATA
data = []
with open("Data - Day05.txt") as file:
    for line in file:
        data.append(line.strip())
# GOAL 1
"""
Instead of zones or groups, this airline uses binary space partitioning to seat people. 
A seat might be specified like FBFBBFFRLR, where F means "front", B means "back",
L means "left", and R means "right".

The first 7 characters will either be F or B; 
these specify exactly one of the 128 rows on the plane (numbered 0 through 127). 
Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; 
the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). 
The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). 
The same process as above proceeds again, this time with only three steps. 
L means to keep the lower half, while R means to keep the upper half.

Every seat also has a unique seat ID: multiply the row by 8, then add the column.

As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
""" 
def find_seatID(seat, rows=128, cols=8):
    rows = list(range(rows))
    cols = list(range(cols))

    for i in seat:
        if i == "B":
            div = int(len(rows)/2)
            rows = rows[div:]
        elif i == "F":
            div = int(len(rows)/2)
            rows = rows[:div]
        elif i == "R":
            div = int(len(cols)/2)
            cols = cols[div:]
        elif i == "L":
            div = int(len(cols)/2)
            cols = cols[:div]

    return rows[0] * 8 + cols[0]

def part1(data):
    seat = ""
    while len(seat) < 7:
        old_len = len(seat)
        regex = "^" + seat + "B"
        for i in data:
            if re.search(regex, i):
                seat = seat + "B"
                break

        if old_len == len(seat):
            seat = seat + "F"

    while 7 <= len(seat) < 10:
        old_len = len(seat)
        regex = "^" + seat + "R"
        for i in data:
            if re.search(regex, i):
                seat = seat + "R"
                break

        if old_len == len(seat):
            seat = seat + "L"

    return find_seatID(seat), seat
    

print(f"The max seatID is {part1(data)[0]} on seat {part1(data)[1]}")

# GOAL 2
"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, 
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""
def all_seat_ids(data):
    ids = []
    for i in data:
        ids.append(find_seatID(i))

    return sorted(ids)

def part2(data):
    ids = all_seat_ids(data)
    for i in list(range(ids[0], ids[-1] + 1)):
        if i not in ids:
            print(f"My seat is at id {i}")

part2(data)

