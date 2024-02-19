def generator(num):
    for i in range(num):
        i+=1
        yield i**2
num = int(input())
for res in generator(num):
    print(res, end=" ")