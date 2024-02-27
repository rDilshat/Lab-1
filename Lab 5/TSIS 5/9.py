import re
def splitting(s):
    result = re.split('(?=[A-Z])', s)
    return result
string = input()
result_list = splitting(string)
result_string = ' '.join(result_list)
print(result_string)