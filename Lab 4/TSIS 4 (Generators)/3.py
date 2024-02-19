def generator(num):
    for i in range(num):
        if(i%3==0 and i%4==0):
            yield i
num = int(input())
for res in generator(num):
    print(res)