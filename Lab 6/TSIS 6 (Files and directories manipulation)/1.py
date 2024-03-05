import os
def checker(path):
    try:
        entries = os.listdir(path)
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print("Error: " + str(path) + " doesn't exist")
path = input("Enter the path: ")
checker(path)