def reverseString():
    a = input()
    words = a.split()
    words.reverse()

    for i in words:
        print(i, end=" ")

reverseString()