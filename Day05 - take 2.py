# I discovered that I solved this problem the hard way. I want to try the easiest solution involving converting things to binary.

# DATA
data = []
with open("Data - Day05.txt") as file:
    for line in file:
        binum = "0b"
        for char in line:
            if char == "B" or char == "R":
                binum += "1"
            elif char == "F" or char == "L":
                binum += "0"
        data.append(binum)
        
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
def part1(data):
    max_val = 0
    for i in data:
        val = int(i[2:], 2) 
        if val > max_val:
            max_val = val
    return max_val

print(f"The max seatID equals {part1(data)}")

# GOAL 2:
"""
It's a completely full flight, so your seat should be the only missing boarding pass in your list. 
However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, 
so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""
def part2(data):
    int_vals = []
    for i in data:
        int_vals.append(int(i[2:], 2))
    
    ids = sorted(int_vals)

    for i in list(range(ids[0], ids[-1] + 1)):
        if i not in ids:
            print(f"My seat is at id {i}")
part2(data)