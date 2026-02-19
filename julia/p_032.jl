# Project euler 32. problem

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 
# 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity,39 x 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

function euler32()
    NoPandigitals = 0
    for i in 1:10^5
        if HasPandigitalProduct(i) == 1
            NoPandigitals += i
        end
    end
    return NoPandigitals
end

function HasPandigitalProduct(a::Number)
    for count in 1:(sqrt(a) + 1)
        if a % count == 0
            NumberString = string(Int(a)) * string(Int(count)) * string(Int(a ÷ count))
            if join(sort(collect(NumberString))) == "123456789"
                return 1
            end
        end
    end
    return 0
end


@time show(euler32())