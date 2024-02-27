import re
def match_string(pattern, string):
    match = re.match(pattern, string)
    if match:
        print("String satisfies the condition")
    else:
        print("String doesn't satisfy the condition")
pattern = r'ab*'
string = input()
match_string(pattern, string)