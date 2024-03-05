import os
def delete(file):
    try:
        if os.path.exists(file):
                os.remove(file)
                print(f"File '{file}' has been deleted")
        else:
            print(f"Error: The specified file '{file}' doesn't exist")
    except Exception as a:
        print(f"Error: {a}")
s = input("Enter the path: ")
delete(s)