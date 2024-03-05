def writelist(filename, lst):
    try:
        with open(filename, 'w') as file:
            for item in lst:
                file.write(str(item) + '\n')
        print("List has been written to", filename)
    except IOError:
        print("Error writing to file.")

my_list = ['apple', 'banana', 'orange', 'grape']
writelist('output.txt', my_list)