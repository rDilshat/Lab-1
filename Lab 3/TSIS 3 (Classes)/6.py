def isPrime(a):
    if(a <= 1):
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if(a%i == 0):
            return False
    return True

numbers = []
a = int(input())

for i in range(a):
    b = int(input())
    numbers.append(b)

primes = list(filter(lambda x: isPrime(x), numbers))
print(primes)