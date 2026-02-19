import itertools

def solve():
    nums = set(range(1, 11))
    best = ""

    for inner in itertools.permutations(range(1, 11), 5):
        inner = list(inner)
        outer_nums = list(nums - set(inner))

        # outer ring must include 10 to ensure 16 digits
        if 10 not in outer_nums:
            continue

        for outer in itertools.permutations(outer_nums):
            outer = list(outer)

            # compute line sums
            s = outer[0] + inner[0] + inner[1]
            if (outer[1] + inner[1] + inner[2] != s or
                outer[2] + inner[2] + inner[3] != s or
                outer[3] + inner[3] + inner[4] != s or
                outer[4] + inner[4] + inner[0] != s):
                continue

            # build triplets
            lines = [
                (outer[0], inner[0], inner[1]),
                (outer[1], inner[1], inner[2]),
                (outer[2], inner[2], inner[3]),
                (outer[3], inner[3], inner[4]),
                (outer[4], inner[4], inner[0]),
            ]

            # rotate so that the smallest outer node starts
            min_index = min(range(5), key=lambda i: lines[i][0])
            lines = lines[min_index:] + lines[:min_index]

            # create concatenated string
            candidate = "".join("".join(map(str, line)) for line in lines)

            # must be 16-digit
            if len(candidate) == 16 and candidate > best:
                best = candidate

    return best

print(solve())