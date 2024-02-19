import math
def area(n, s):
    return 0.25 * n * s**2 * (math.tan(math.pi/n))**(-1)
print("Input numbers of side: ", end="")
n = float(input())
print("Input the length of a side: ", end="")
s = float(input())
print("The are of the polygon is:", area(n,s))