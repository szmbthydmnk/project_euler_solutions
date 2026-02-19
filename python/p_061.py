print("Project Euler Problem 61:\n " \
"Find the unique cyclic set of six 4-digit numbers, each a different figurate number type (triangle, square, pentagonal, hexagonal, heptagonal, octagonal), where the last two digits of each number are the first two digits of the next, forming a cycle.")
import itertools


def polygonalNumber(Index: int, degree: int):
    return int(0.5 * Index * ((degree - 2) * Index + (4 - degree)))

def is_polygonalNumber(n: int, degree: int) -> bool:
    """
    Checks if n is a polygonal number of the given degree.
    Uses the quadratic formula to solve for Index (k) in:
        n = 0.5 * k * ((degree - 2) * k + (4 - degree))
    Rearranged:
        (degree - 2) * k^2 + (4 - degree) * k - 2n = 0
    """
    a = degree - 2
    b = 4 - degree
    c = -2 * n
    # Quadratic formula: k = [-b ± sqrt(b^2 - 4ac)] / (2a)
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return False
    sqrt_discriminant = discriminant ** 0.5
    if sqrt_discriminant % 1 != 0:
        return False
    k = (-b + sqrt_discriminant) / (2 * a)
    # k must be a positive integer
    return k > 0 and k % 1 == 0


# Polygonal degrees
degrees = [3, 4, 5, 6, 7, 8]

# Generate all 4-digit polygonal numbers for each type
# We'll only consider numbers in [1000, 9999]
polygonals = {}  # degree: set of 4-digit numbers
for deg in degrees:
    nums = set()
    n = 1
    while True:
        poly = polygonalNumber(n, deg)
        if poly > 9999:
            break
        if 1000 <= poly <= 9999:
            nums.add(poly)
        n += 1
    polygonals[deg] = nums

# For fast lookup by prefix (first two digits), build a mapping
# polygonal_by_prefix[degree][prefix] = set of numbers with that prefix
polygonal_by_prefix = {}
for deg in degrees:
    dct = {}
    for num in polygonals[deg]:
        prefix = num // 100
        dct.setdefault(prefix, set()).add(num)
    polygonal_by_prefix[deg] = dct

# For fast lookup by suffix (last two digits), build a mapping
# polygonal_by_suffix[degree][suffix] = set of numbers with that suffix
polygonal_by_suffix = {}
for deg in degrees:
    dct = {}
    for num in polygonals[deg]:
        suffix = num % 100
        dct.setdefault(suffix, set()).add(num)
    polygonal_by_suffix[deg] = dct


# Backtracking search to build a cycle of six numbers, one from each polygonal type,
# where the last two digits of one match the first two digits of the next,
# and all six polygonal types are used exactly once.

def search(chain, used_degrees):
    """
    chain: list of numbers in the current chain
    used_degrees: list of degrees used so far (same order as chain)
    """
    # Base case: if chain has 6 numbers, check wraparound
    if len(chain) == 6:
        # Last two digits of last must match first two digits of first
        if chain[-1] % 100 == chain[0] // 100:
            # Found a solution!
            print("Cyclic sequence found:")
            for d, n in zip(used_degrees, chain):
                print(f"{n} ({d}-gon)")
            print("Sum:", sum(chain))
            return True  # stop at first solution
        return False

    # Next, try to extend the chain
    last = chain[-1]
    suffix = last % 100
    if suffix < 10:
        # Next number would not be a 4-digit number (prefix would be 0X)
        return False

    # Try every unused degree
    for deg in degrees:
        if deg in used_degrees:
            continue
        # Find all numbers of this degree with prefix == suffix
        candidates = polygonal_by_prefix[deg].get(suffix, set())
        for num in candidates:
            if num in chain:
                continue  # avoid using same number twice
            if search(chain + [num], used_degrees + [deg]):
                return True  # stop after first solution
    return False


# Try all permutations of the degrees, and for each, try all possible starting numbers
# To avoid duplicate cycles (rotations), fix the first degree to be 3 (triangle)
first_deg = 3
other_degrees = [d for d in degrees if d != first_deg]

found = False
for perm in itertools.permutations(other_degrees):
    deg_order = [first_deg] + list(perm)
    for start_num in polygonals[first_deg]:
        # The chain and used_degrees are in parallel
        if search([start_num], [first_deg]):
            found = True
            break
    if found:
        break




