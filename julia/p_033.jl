function Digit_Cancelling(Nominator, Denominator)
    Digits_Nominator    = digits(Nominator)
    Digits_Denominator  = digits(Denominator)
    for i in 1:length(Digits_Nominator)
        for j in 1:length(Digits_Denominator)
            if Digits_Nominator[i] == Digits_Denominator[j] && Digits_Nominator[i] != 0
                temp_Nominator      = Digits_Nominator[1 + length(Digits_Nominator) - i]
                temp_Denominator    = Digits_Denominator[1 + length(Digits_Denominator) - j]
                
                if temp_Nominator/temp_Denominator == Nominator/Denominator
                    return true
                end
            end
        end
    end
    return false
end


Nominator   = 1
Denominator = 1
for n in 10:99
    for d in (n + 1):99
        if Digit_Cancelling(n, d)
            Nominator *= n
            Denominator *= d
        end
    end
end

gcd_num = gcd(Nominator, Denominator)
print(Denominator/gcd_num)
























# Function to compute the greatest common divisor
function gcd(a, b)
    while b != 0
        a, b = b, a % b
    end
    return a
end

# Check if two fractions (numerator/denominator) are digit-cancelling fractions
function is_digit_cancelling(n, d)
    n_digits = digits(n)  # Get digits of numerator
    d_digits = digits(d)  # Get digits of denominator
    
    for i in 1:length(n_digits)
        for j in 1:length(d_digits)
            if n_digits[i] == d_digits[j] && n_digits[i] != 0
                # Cancel the common digit and check if the simplified fraction is correct
                new_n = n_digits[3-i]  # Other digit of numerator
                new_d = d_digits[3-j]  # Other digit of denominator
                if new_d != 0 && n * new_d == d * new_n
                    return true
                end
            end
        end
    end
    return false
end

# Collect the product of the valid fractions
numerator_product = 1
denominator_product = 1

for n in 10:99
    for d in (n+1):99  # Fraction should be less than 1, so n < d
        if is_digit_cancelling(n, d)
            numerator_product *= n
            denominator_product *= d
        end
    end
end

# Simplify the final product
g = gcd(numerator_product, denominator_product)
numerator_product = div(numerator_product, g)
denominator_product = div(denominator_product, g)

# Output the denominator of the simplified product
println(denominator_product)