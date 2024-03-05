x = str(input("Enter the string: "))
count_big = 0
count_small = 0
for char in x:
    if char.isupper():
        count_big+=1
    else:
        count_small+=1
print("Number of big letters:", count_big)
print("Number of small letters:", count_small)