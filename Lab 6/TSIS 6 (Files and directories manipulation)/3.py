import os
def checker(path):
    if os.path.exists(path):
        print("Path exists.")
        dirname, filename = os.path.split(path)
        print("Directory portion:", dirname)
        print("Filename portion:", filename)
    else:
        print("Path does not exist.")
path = '1.txt'
checker(path)