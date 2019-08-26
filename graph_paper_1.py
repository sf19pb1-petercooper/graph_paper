
import sys

row = int(input("How many rows of boxes? "))
columns = int(input("How many columns of boxes? "))
row_spaces = int(input("How many rows of spaces in each box? "))
column_spaces = int(input("How many columns of spaces in each box (e.g., 3)? "))


print (row)

for _ in range(row):
    print("+", end=" ")

    for _ in range(columns):
        print("-",end=" ")

        #for space in range(row_spaces):
        #    print("|")

        #for spaces in range(column_spaces):
        #    print(" ")
    
    #print()


#+ and - are characters

sys.exit(0)
