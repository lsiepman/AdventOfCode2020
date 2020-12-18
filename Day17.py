from itertools import product
import operator

# DATA
with open("Data - Day17.txt") as file:
    initial_state = file.read().splitlines() 



# GOAL 1
"""
The pocket dimension contains an infinite 3-dimensional grid. 
At every integer 3-dimensional coordinate (x,y,z), 
there exists a single cube which is either active or inactive.

During a cycle, all cubes simultaneously change their state according to the following rules:

    - If a cube is active and exactly 2 or 3 of its neighbors are also active, 
    the cube remains active. Otherwise, the cube becomes inactive.
    - If a cube is inactive but exactly 3 of its neighbors are active, 
    the cube becomes active. Otherwise, the cube remains inactive.

Starting with your given initial configuration, simulate six cycles. 
How many cubes are left in the active state after the sixth cycle?

"""
active_cors = set()
for (i, row) in enumerate(initial_state):
    for (j, char) in enumerate(row):
        if char == '#':
            active_cors.add((i, j, 0))



def add_tuples(a, b):
    return tuple(x + y for (x, y) in zip(a, b))


def cycle(actives, num_cyc):
    for _ in range(num_cyc):
        temp_storage = set()
        inactives = set()
        neigh = list(product((-1, 0, 1), repeat=len(next(iter(actives)))))
        
        for cube in actives:
            neighbours = set(tuple(map(operator.add, cube, n)) for n in neigh)
            if len(neighbours.intersection(actives)) in [3, 4]: # 2 or 3 neighbours + itself 
                temp_storage.add(cube)
            inactives.update(neighbours.difference(actives))

        for cube in inactives:
            neighbours = set(tuple(map(operator.add, cube, n)) for n in neigh)
            if len(neighbours.intersection(actives)) == 3:
                temp_storage.add(cube)

        actives = temp_storage

    return len(actives)


print(f"After the sixth cycle, {cycle(active_cors, 6)} cubes are left active")

# GOAL 2
"""
Apparently, the pocket dimension actually has four spatial dimensions, not three.
Starting with your given initial configuration, 
simulate six cycles in a 4-dimensional space. 
How many cubes are left in the active state after the sixth cycle?
"""
active_part2 = set()
for (i, row) in enumerate(initial_state):
    for (j, char) in enumerate(row):
        if char == '#':
            active_part2.add((i, j, 0, 0))

print(f"In the 4-dimensional space, {cycle(active_part2, 6)} hypercubes are left active")