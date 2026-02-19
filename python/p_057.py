def problem_57():
    num, den = 3, 2  # first expansion
    count = 0

    for _ in range(1, 1000):
        if len(str(num)) > len(str(den)):
            count += 1
        # recurrence
        num, den = num + 2 * den, num + den

    return count

print(problem_57())