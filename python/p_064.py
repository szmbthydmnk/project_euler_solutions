# Odd Period Square Roots - 2025.10. - Dominik Szombathy


MAX_NUMBER = 1_000_000
odd_period_count = 0

import math

def period_length_sqrt(number):
    """
    Calculate the length of the period of the continued fraction representation of the square root of 'number'.
    Returns 0 if 'number' is a perfect square.
    """
    # Initialize variables for the continued fraction algorithm:
    # m_term: the 'm' variable in the algorithm, initially 0
    # denominator: the 'd' variable in the algorithm, initially 1
    # a0_term: the integer part of the square root of 'number' (floor)
    # a_term: the current integer part of the fraction
    m_term = 0
    denominator = 1
    a0_term = a_term = int(math.isqrt(number))
    
    # If 'number' is a perfect square, its square root is an integer,
    # so the continued fraction has no period.
    if a_term * a_term == number:
        return 0  # perfect square has no period
    
    period = 0
    
    # The process repeats until 'a_term' equals 2 * a0_term,
    # which indicates the period has completed.
    while True:
        # Update m_term using the formula m = d*a - m
        m_term = denominator * a_term - m_term
        
        # Update denominator using the formula d = (number - m^2) / d
        denominator = (number - m_term * m_term) // denominator
        
        # Update a_term using the formula a = floor((a0 + m) / d)
        a_term = (a0_term + m_term) // denominator
        
        period += 1
        
        # When a_term reaches 2 * a0_term, the period repeats
        if a_term == 2 * a0_term:
            break
    
    return period

for n in range(2, MAX_NUMBER + 1):
    if int(math.isqrt(n)) ** 2 == n:
        continue
    if period_length_sqrt(n) % 2 == 1:
        odd_period_count += 1

print("Count of odd period square roots:", odd_period_count)
