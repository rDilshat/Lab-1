import re
def splitting(s):
    result = re.split('(?=[A-Z])', s)
    return result
s = input()
print(splitting(s))