import re
string = input()
r = re.sub('(?:^|_)[a-z]', lambda x: x.group(0).upper(), string)
print(r)