# Project Euler - 90 - Cube Digit Pairs
# Solution by Dominik Szombathy 
# Date - 2026.02.16

# Solution: 1217

# 6 == 9 as we can turn the cube upside down
squares = [
    (0, 1), (0, 4), (0, 6),
    (1, 6), (2, 5), (3, 6),
    (4, 6), (6, 4), (8, 1) 
]

from itertools import combinations

digits = range(10)
cubes = list(combinations(digits, 6))

# len(cubes)            # out: 210

def rotate_nines(cube: list) -> set:
    cube = set(cube)
    if 9 in cube:
        cube.add(6)
        cube.discard(9)
    return cube

def valid_pair(cube1, cube2) -> bool:
    for a, b in squares:
        if not (
            (a in cube1 and b in cube2) or 
            (a in cube2 and b in cube1)
        ):
            return False
    return True
    
distinct_cube_count = 0

for i, _ in enumerate(cubes):
    for j in range(i, len(cubes)):
        c1 = rotate_nines(cubes[i])
        c2 = rotate_nines(cubes[j])
        
        if valid_pair(c1, c2):
            distinct_cube_count += 1

print(distinct_cube_count)