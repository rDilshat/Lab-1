def unique(nums):
    for key, value in nums.items(): 
        if(value == 1):
            print(key, end=" ")
def main():
    n = int(input())
    mp = {}

    for i in range(n):
        a = int(input())
        mp[a] = mp.get(a, 0) + 1

    unique(mp)

main()