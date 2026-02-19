keylogs = [319,
680,
180,
690,
129,
620,
762,
689,
762,
318,
368,
710,
720,
710,
629,
168,
160,
689,
716,
731,
736,
729,
316,
729,
729,
710,
769,
290,
719,
680,
318,
389,
162,
289,
162,
718,
729,
319,
790,
680,
890,
362,
319,
760,
316,
729,
380,
319,
728,
716]




numbers = set()
for n in keylogs:
    for i in str(n):
        numbers.add(str(i))

print(numbers)
number_of_unique_numbers        = len(numbers)
number_of_unique_combinations   = len(set(keylogs))

print("Number of different digits: ", number_of_unique_numbers)
print("Number of different combinations: ", number_of_unique_combinations)

graph = {}
weights = {}
for keys in keylogs:
    k = str(keys)
    for i in range(len(k)-1):
        a, b = k[i], k[i + 1]
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        if b not in graph[a]:
            graph[a].add(b)
            weights[b] = weights.get(b, 0) + 1
        if a not in weights:
            weights[a] = weights.get(a, 0)


print(graph)
print(weights)
        
queue = [node for node in weights if weights[node] == 0]  
print(queue)

passcode = ''
while queue:
    node = queue.pop(0)  # pop first element (like a queue)
    passcode += node
    print(passcode)
    for neighbor in graph[node]:
        weights[neighbor] -= 1
        if weights[neighbor] == 0:
            queue.append(neighbor) 

print(passcode)

