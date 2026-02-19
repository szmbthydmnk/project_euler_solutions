using ProjectEuler
question(38)

ans = ""
for Number in 2:9
    for i in 1:10^(Int(floor(9/Number)))
        s = join(string(i * j) for j in 1:Number)
        if join(sort(collect(s))) == "123456789"
            ans = max(s, ans)
        end
    end
end

println(ans)