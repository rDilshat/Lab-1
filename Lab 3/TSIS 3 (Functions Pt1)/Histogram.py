def histogram(a):
    for i in range(a):
        print("*", end="")

size = int(input())
arr = []

for i in range(size):
    a = int(input())
    arr.append(a)

for i in range(len(arr)):
    histogram(arr[i])
    print()