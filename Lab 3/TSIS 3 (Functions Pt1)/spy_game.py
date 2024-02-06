def spy_game(nums):
    checker = ""
    for i in range(len(nums)):
        if(nums[i]=='0' or nums[i]=='7'):
            checker+=nums[i]
            if(checker == "007"):
                return True
    return False

def main():
    nums = []
    a = int(input())
    for i in range(a):
        b = input()
        nums.append(b)
    if(spy_game(nums)):
        print("True")
    else:
        print("False")
main()