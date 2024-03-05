import os

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in letters:
    with open(i + ".txt", 'w') as file:
        file.write(f"This is {i} file")