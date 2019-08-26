import sys

row = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
row_spaces = int(input("How many rows of spaces in each box? "))
column_spaces = int(input("How many columns of spaces in each box (e.g., 3)? "))


even_line = ('+' + ('-' * column_spaces)) * row_spaces
odd_line = ('|' + (' ' * column_spaces)) * row_spaces
for i in range(row):
    if i % 2 == 0:
        print(even_line)
    else:
        print(odd_line)


sys.exit(0)
