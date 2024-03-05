import os

def lines(name_file):
    try:
        with open(name_file, 'r') as file:
            linecount = sum(1 for i in file)
            print("The number of lines in the file " + str(name_file) + " is "+ str(linecount))
    except FileNotFoundError:
        print("Error: The file " + str(name_file) + " does not exist.")
name_file = input("Enter the path to the text file: ")
lines(name_file)