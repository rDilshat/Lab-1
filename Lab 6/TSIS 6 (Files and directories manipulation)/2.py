import os
def checker(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Read access:", os.access(path, os.R_OK))
        print("Write access:", os.access(path, os.W_OK))
        print("Execute access:", os.access(path, os.X_OK))
    else:
        print("Path does not exist.")
path = '1.txt'
checker(path)