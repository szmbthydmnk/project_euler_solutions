# problem 014: Find the longest Collatz number chain starting from a number under a million
# making one step in the right direction :)
def step(num):
    if num % 2 == 0:
        return int(num/2)
    else:
        return (3*num + 1)

# the idea was to calculate only unique Collatz chains, and when the code
# encounters a number thats been calculated before it will just add the number of
# steps from that previously calculated sequence.

#Runs about 1 - 1.2 seconds on my pc, but I guess one could get a more clever approach

def euler14(N):
    sequence_length = []
    for i in range(1, N):
        length = 1
        num = i
        while num != 1:
            num = step(num)
            if num < i :
                length += sequence_length[num - 1]
                break
            length += 1
        sequence_length.append(length)
    return max(sequence_length), len(sequence_length), sequence_length.index(max(sequence_length))+1

print(euler14(10 ** 6))
