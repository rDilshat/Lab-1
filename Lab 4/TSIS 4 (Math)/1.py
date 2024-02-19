import math
def calculate(a):
    return a * (math.pi/180)
num = int(input())
print(round(calculate(num), 6))