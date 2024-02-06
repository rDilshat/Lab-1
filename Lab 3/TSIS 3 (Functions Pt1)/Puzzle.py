def solve(numheads, numlegs):
    numchickens = 0
    while(numheads <= numlegs):
        numrabbits = numheads - numchickens
        if(numchickens * 2) + (numrabbits * 4) == numlegs:
            return numchickens, numrabbits
        numchickens += 1
    return "No Solution"

numheads = int(input())
numlegs = int(input())
result = solve(numheads, numlegs)
print(result)