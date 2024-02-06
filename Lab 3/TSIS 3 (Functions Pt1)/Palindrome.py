def isPalindrome():
    a = str(input())
    b = ''.join(reversed(a))
    if a == b:
        print("Palindrome")
    else:
        print("Not Palindrome")

isPalindrome()