def filter_prime(a):
    if (a <= 1):
        return False
    for i in range(2, int(a**0.5) + 1):
        if(a % i == 0):
            return False
    return True
 
def main():
    a = int(input())
    arr = []
    
    for i in range(a):
        b = int(input())
        arr.append(b)
    
    for i in range(0, len(arr)):
        if(filter_prime(arr[i])):
            print(arr[i])

main()