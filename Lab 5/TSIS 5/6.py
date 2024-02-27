import re

string = input()
r = re.sub('[ ,.]', ':', string)
print(r)