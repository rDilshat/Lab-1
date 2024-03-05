a = int(input("Enter size of list: "))
arr = []
print("Enter elements: ")
for i in range(a):
    b = int(input())
    arr.append(b)
count = 1
for i in range(a):
    count *= arr[i]
print(count)