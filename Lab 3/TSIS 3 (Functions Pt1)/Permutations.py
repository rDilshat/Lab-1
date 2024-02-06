from itertools import permutations

def permiki(s):
    perms = permutations(s)

    for i in perms:
        print(''.join(i))

def main():
    s = input()
    permiki(s)

main()