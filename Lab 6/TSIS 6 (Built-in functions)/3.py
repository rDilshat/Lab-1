def isPalindrome(a):
    b = a[::-1]
    if a == b:
        print("Palindrome")
    else:
        print("Not palindrome")
a = str(input())
isPalindrome(a)