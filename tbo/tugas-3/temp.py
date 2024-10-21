language = {'A', 'B', 'C'}  # Set of single-character strings
x = 65  # ASCII code for 'A'

if chr(x) in language:
    print("Found!")
else:
    print("Not found")