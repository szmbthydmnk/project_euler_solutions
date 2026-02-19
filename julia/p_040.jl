using LinearAlgebra
using ProgressBars

# Brute force, constrcut the number, then calculate whatever
function champernowne_digit_at(n)
    digits_per_number = 1
    count = 9
    while n > digits_per_number * count
        n -= digits_per_number * count
        digits_per_number   += 1
        count               *= 10
    end
    n -= 1  # zero-based index in the block
    start_num   = 10^(digits_per_number - 1)
    num         = start_num + n ÷ digits_per_number
    digit_pos   = n % digits_per_number
    
    s = string(num)
    return parse(Int, s[digit_pos+1])
end

function clever_champernowne()
    indices = [1,10,100,1000,10000,100000,1000000]
    digits = [digit_at(i) for i in indices]
    return prod(digits)
end

clever_champernowne()