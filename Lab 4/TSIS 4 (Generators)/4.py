def squares(a, b):
    for i in range(a, b):
        yield i**2
a = int(input())
b = int(input())
for res in squares(a, b):
    print(res, end = " ")