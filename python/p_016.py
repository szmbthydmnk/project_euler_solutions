

def euler16():
    num = str(2**1000)
    s = sum( int(num[i]) for i in range(len(num)))
    return s

print(euler16())
