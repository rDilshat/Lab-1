import re
def string_match(pattern, string):
    match = re.search(pattern, string)
    if match:
        print("String satisfies condtition")
    else:
        print("String doesn't satisfy condition")
pattern = r'.a.b$'
string = input()
string_match(pattern, string)