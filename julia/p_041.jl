using ProjectEuler
using Combinatorics
question(41)

function VV2VI(V::Vector)
    return foldl((a, d) -> a*10 + d, V,; init = 0)
end

function Generate_N_Pandigital_Number(N::Int)
    Numbers = 1:N;
    return collect(permutations(Numbers, N))
end

function IsPrime(Number::Int)
    DivisionCheckLimit = ceil(sqrt(Number))
    for Divisors in 3:DivisionCheckLimit
        if Number % Divisors == 0
            return false
        end
    end
    return true
end

biggestPrime = 0
for OrderOfMagnitude in 1:9
    Pandigitals = Generate_N_Pandigital_Number(OrderOfMagnitude)

    for n in Pandigitals
        global number = VV2VI(n)
        if IsPrime(number)
            if number > biggestPrime
                biggestPrime = number
            end
        end
    end
end
biggestPrime