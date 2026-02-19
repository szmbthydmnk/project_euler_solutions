MaxNumber = 1000000

function is_symmetric(Number::Int)
    Number_string = string(Number)
    return Number_string == reverse(Number_string)
end

Sum = 0
for N in 1:MaxNumber
    if is_symmetric(N)
        if digits(N, base=2) == digits(N, base=2) |> reverse
            Sum += N
        end
    end
end

println(Sum)