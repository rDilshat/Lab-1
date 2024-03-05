def copy(source1, source2):
    try:
        with open(source1, 'r') as source:
            with open(source2, 'w') as destination:
                destination.write(source.read())
        print("Contents copied from", source1, "to", source2)
    except IOError:
        print("Error copying file.")
source1 = '1.txt'
source2 = '2.txt'
copy(source1, source2)