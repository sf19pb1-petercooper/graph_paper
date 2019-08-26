
import sys

rows = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
row_spaces = int(input("How many rows of spaces in each box? "))
column_spaces = int(input("How many columns of spaces in each box (e.g., 3)? "))


for i in range(rows):
	for i in range(columns):
	    print("+",end="")
	    for i in range(column_spaces):
	        print("-",end="")
	print("+")

	for spaces in range(row_spaces):
	    for _ in range(columns):
	        print("|",end="")

	        for space in range(column_spaces):
	            print(" ",end="")
	    
	    print("|")

for i in range(columns):
    print("+",end="")
    for i in range(column_spaces):
        print("-",end="")
print("+")

#+ and - are characters

sys.exit(0)
