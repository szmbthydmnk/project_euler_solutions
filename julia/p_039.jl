using LinearAlgebra
using Plots
using Statistics
using StatsBase

function euler39()
    p = Vector{Int64}()
    for a in 1:100000
        for b in 1:100000
            c = sqrt(a^2 + b^2)
            if isinteger(c)
                push!(p, a + b + c)
            end
        end
    end

    mode(p)
end

@time show(euler39)