time_taken = @elapsed begin


using Primes

NumberOfPrimes  = 0
Number          = 10

SumOfTruncatedPrimes = 0

while NumberOfPrimes < 11
    if isprime(Number)
        Number_String = string(Number)
        NumberLength = length(Number_String)
        
        Left_Prime = 1
        Right_Prime = 1
        for i in 1:NumberLength-1
            Truncated_Number_Right = parse(Int, Number_String[i+1:end])            
            Truncated_Number_Left = parse(Int, Number_String[1:end-i])
            if isprime(Truncated_Number_Left) == false
                Left_Prime = 0
            end
            if isprime(Truncated_Number_Right) == false
                Right_Prime = 0
            end
        end

        if Right_Prime + Left_Prime == 2
            NumberOfPrimes += 1
            println("N: ", NumberOfPrimes, " - ", Number)
            SumOfTruncatedPrimes += Number
        end
    end
    Number += 1
end

println(SumOfTruncatedPrimes)
end
println("Execution time:", time_taken, "seconds")