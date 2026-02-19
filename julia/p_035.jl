using Primes
using ProgressMeter

function get_circular_combinations(Number)
    digit_list = digits(Number)
    Combinations = []

    for i in 1:length(digit_list)
        rotated_digits = vcat(digit_list[i:end], digit_list[1:i-1])
        if rotated_digits[1] != 0
            push!(Combinations, parse(Int, join(rotated_digits)))
        end
    end
    return Combinations
end

function consist_even_digit(Number)
    digit_str = string(Number)
    for digit in digit_str
        if parse(Int, digit) % 2 == 0 && parse(Int, digit) != 0
            return true
        end
    end
    return false
end

NumberOfCircularPrimes = 4

@showprogress for N in 10:99999

    if !consist_even_digit(N)
        if isprime(N)
            Combinations = get_circular_combinations(N)
            k = 1
            for comb in Combinations
                if isprime(comb)
                    k *= 1
                else
                    k *= 0
                end
            end
            NumberOfCircularPrimes += k
        end
    end
end

println(NumberOfCircularPrimes)