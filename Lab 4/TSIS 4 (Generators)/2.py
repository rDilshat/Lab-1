def generator(num):
    for i in range(num):
        if(i%2==0):
            yield i
num = int(input())
for res in generator(num):
    print(res)