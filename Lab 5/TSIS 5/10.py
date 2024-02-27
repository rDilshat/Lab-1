import re
string = input()
r = re.sub('(?<!^)(?=[A-Z])', '_', string).lower()
print(r)