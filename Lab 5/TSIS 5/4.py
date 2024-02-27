import re
def string_match(pattern, string):
    match = re.search(pattern, string)
    if match:
        print("String satisfies the condition")
    else:
        print("String doesn't satisfy the condition")
pattern = r'[A-Z][a-z]+$'
string = input()
string_match(pattern, string)