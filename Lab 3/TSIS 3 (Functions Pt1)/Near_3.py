def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == 3 and nums[i+1] == 3):
            return True
        elif(nums[i] == 3 and nums[i-1] == 3):
            return True
    return False

def main():
    a = int(input())
    nums = []

    for i in range(a):
        b = int(input())
        nums.append(b)

    if(has_33(nums)):
        print("True")
    else:
        print("False")

main()