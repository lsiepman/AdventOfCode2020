data = []
with open("Data - Day12.txt") as file:
    for line in file:
        data.append(line.strip())

# GOAL 1
"""
The navigation instructions (your puzzle input) consists of a sequence of single-character actions paired with integer input values. 
After staring at them for a few minutes, you work out what they probably mean:

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.

The ship starts by facing east. Only the L and R actions change the direction the ship is facing.

Figure out where the navigation instructions lead. 
What is the Manhattan distance between that location and the ship's starting position?
"""

def turn(curr_facing, instruction):
    directions = {"E": 0, "N": 90, "W": 180, "S": 270,
                   0: "E", 90: "N", 180: "W", 270: "S"} # unit circle
    
    face_val = directions[curr_facing]    
    
    if "L" in instruction:
        new_face_val = (face_val + int(instruction[1:])) % 360
    elif "R" in instruction:
        new_face_val = (face_val - int(instruction[1:])) % 360

    return directions[new_face_val]

def move(curr_facing, instruction, N_val, E_val):    
    if "F" in instruction:
        if curr_facing == "E":
            E_val += int(instruction[1:])
        elif curr_facing == "W":
            E_val -= int(instruction[1:])
        elif curr_facing == "N":
            N_val += int(instruction[1:])
        elif curr_facing == "S":
            N_val -= int(instruction[1:])

    elif "N" in instruction:
        N_val += int(instruction[1:])
    elif "S" in instruction:
        N_val -= int(instruction[1:])
    elif "E" in instruction:
        E_val += int(instruction[1:])
    elif "W" in instruction:
        E_val -= int(instruction[1:])

    return N_val, E_val

def calc_manhattan(N_val, E_val):
    return abs(N_val) + abs(E_val)

def part1(data, curr_facing="E"):
    N_val = 0
    E_val = 0

    for i in data:
        if "L" in i or "R" in i:
            curr_facing = turn(curr_facing, i)
        else:
            N_val, E_val = move(curr_facing, i, N_val, E_val)

    return calc_manhattan(N_val, E_val)

print(f"The ferry ends up {part1(data)} units from its initial position")

# GOAL2
"""
Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:

    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

The waypoint starts 10 units east and 1 unit north relative to the ship. 
The waypoint is relative to the ship; that is, if the ship moves, the waypoint moves with it.

Figure out where the navigation instructions actually lead. 
What is the Manhattan distance between that location and the ship's starting position?
"""
def rotate(N_val, E_val, instruction):
    if "L" in instruction:
        if "90" in instruction:
            new_E_val = -N_val
            new_N_val = E_val
        elif "180" in instruction:
            new_E_val = -E_val
            new_N_val = -N_val
        elif "270" in instruction:
            new_E_val = N_val
            new_N_val = -E_val
    
    elif "R" in instruction:
        if "270" in instruction:
            new_E_val = -N_val
            new_N_val = E_val
        elif "180" in instruction:
            new_E_val = -E_val
            new_N_val = -N_val
        elif "90" in instruction:
            new_E_val = N_val
            new_N_val = -E_val

    return new_N_val, new_E_val

def towards_waypoint(way_N, way_E, ship_N, ship_E, instruction):
    new_ship_N = int(instruction[1:]) * way_N + ship_N
    new_ship_E = int(instruction[1:]) * way_E + ship_E

    return new_ship_N, new_ship_E

def part2(data):
    ship_N = 0
    ship_E = 0
    way_E = 10
    way_N = 1

    for i in data:
        if "F" in i:
            ship_N, ship_E = towards_waypoint(way_N, way_E, ship_N, ship_E, i)
        elif "L" in i or "R" in i:
            way_N, way_E = rotate(way_N, way_E, i)
        else:
            way_N, way_E = move("no", i, way_N, way_E)

    return calc_manhattan(ship_N, ship_E)

print(f"Now the ship is {part2(data)} units from its initial position")