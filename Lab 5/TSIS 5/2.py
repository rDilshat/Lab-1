import re
def match_string(pattern, string):
    match = re.search(pattern, string)
    if match:
        print("String satisfies the condition")
    else:
        print("String doesn't satisfy the condition")
pattern = r'abbb*'
string = input()
match_string(pattern, string)