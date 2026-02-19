def is_symmetric(Number):
    Number_string = str(Number)
    return list(str(Number)) == list(reversed(Number_string))

def get_circular_combinations(Number):
    digits = [int(d) for d in str(Number)]
    Combinations = []

    for i in range(len(digits)):
        rotated_digits = digits[i:] + digits[:i]

        if rotated_digits[0] != 0:
            Combinations.append(int("".join(map(str, rotated_digits))))
    
    return Combinations

def consist_even_digit(Number):
    digit_str = str(Number)
    for digit in str(Number):
        if int(digit) % 2 == 0 and int(digit) != 0:
            return True
    return False

def NumOfDivisors(num):
    divisors = 2
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            divisors += 2
            if i == np.sqrt(num):
                divisors -= 1
    return divisors

def Divisors(num):
    if isinstance(num, int) == True:
        divs = [1]
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                divs.append(i)
    else:
        print('Not integer :(')
    return divs

def IsAbundant(num):
    divs = Divisors(num)
    if sum(divs) > num:
        return True
    else:
        return False

def FibonacciSequence(a0, a1, N):
    Seq = []
    Seq.append(1)
    Seq.append(1)

    if a0 == 0 || a1 == 0:
        for i in range(3, N):
            Seq.append(Seq[-1] + Seq[-2])

        return Seq
    elif N == 0:
        print(' Start from at least 3 pls')
    else:
        return a0 + a1

def digit_by_digit_sqrt(n : int, precision: int) -> list[int]:
    NumberPairs = []
    n_str = str(n)
    if len(n_str) % 2 == 1:
        n_str = '0' + n_str

    for i in range(0, len(n_str), 2):
        NumberPairs.append(int(n_str[i:i + 2]))
    
    for _ in range(precision):
        NumberPairs.append(0)

    NumberSqrt = []
    Remainder = 0
    Root = 0
    for pair in NumberPairs:
        Remainder = Remainder * 100 + pair

        NextDigit = 0

        Divisor = Root * 20
        for k in range(9, -1, -1):
            if (Divisor + k) * k <= Remainder:
                NextDigit = k
                break
        NumberSqrt.append(NextDigit)
        Remainder -= (Divisor + NextDigit) * NextDigit
        Root = Root * 10 + NextDigit
    return NumberSqrt

def generate_primes_up_to(limit: int) -> list[int]:
    """
    Generate all prime numbers up to 'limit' (inclusive).

    Args:
        limit (int): the upper bound

    Returns:
        list[int]: list of primes up to limit
    """
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes

    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False

    return [i for i, prime in enumerate(sieve) if prime]


def Roman_to_Integer(roman: str) -> int:
    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = RomanToIntMap[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

def Integer_to_Roman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ""
    for i in range(len(values)):
        while num >= values[i]:
            roman_numeral = roman_numeral + symbols[i]
            num -= values[i]
    return roman_numeral