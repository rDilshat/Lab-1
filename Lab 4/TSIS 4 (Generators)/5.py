def generator(num):
    for i in range(0, num + 1):
        i = num - i
        yield i
num = int(input())
for res in generator(num):
    print(res, end=" ")