# First taking input from user
table = [[1 for i in range(9)] for j in range(9)]

file =open("input.txt","r")
table = [[1 for i in range(9)] for j in range(9)]
i = -1
j = -1
with file as fileobj:
    for line in fileobj:
        i=i+1
        j=-1
        for ch in line:
            if(ch=="\n"):
                continue
            j=j+1
            table[i][j] = int(ch)
print(table)
k = 4
while (k != 0):
    # This while loop is used to work the following processes in k times
    for row in range(9):
        for col in range(9):

            a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Here elements in array is integer type
            if (table[row][col] == 0):  # Here checking the empty boxes, if it is zero the following program will work

                for i in table[row][:]:  # Checking elements in a row

                    b = int(i)  # elements in the table are str type , so converting them to int type
                    if (b in a):  # since a and b are int type comparing them to remove b from a
                        a.remove(b)

                for j in range(9):  # Checking elements in a column

                    c = int(table[j][col])
                    if (c in a):
                        a.remove(c)
                # The following program is for identifying each 3x3 boxes for corresponding box, 
                # Let row and col indicate the row and column of the table where element is zero
                # Then the corresponding 3x3 boxes will get as,
                # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                if ((row + 1) % 3 == 1):
                    if ((col + 1) % 3 == 1):

                        for i in range(3):
                            for j in range(3):

                                d = int(table[row + i][col + j])
                                if (d in a):
                                    a.remove(d)

                    # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                    # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                    elif ((col + 1) % 3 == 2):

                        for i in range(3):
                            for j in range(-1, 2):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)

                    # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                    # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                    elif ((col + 1) % 3 == 0):
                        #print("")
                        for i in range(3):
                            for j in range(-2, 1):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)

                # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                if ((row + 1) % 3 == 2):

                    if ((col + 1) % 3 == 1):

                        for i in range(-1, 2):

                            for j in range(3):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)



                    # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                    # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                    elif ((col + 1) % 3 == 2):

                        for i in range(-1, 2):

                            for j in range(-1, 2):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)

                    # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                    # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                    elif ((col + 1) % 3 == 0):

                        for i in range(-1, 2):

                            for j in range(-2, 1):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)

                # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                if ((row + 1) % 3 == 0):
                    if ((col + 1) % 3 == 1):

                        for i in range(-2, 1):
                            for j in range(3):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)


                    # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                    # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                    elif ((col + 1) % 3 == 2):

                        for i in range(-2, 1):
                            for j in range(-1, 2):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)

                    # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                    # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                    elif ((col + 1) % 3 == 0):

                        for i in range(-2, 1):
                            for j in range(-2, 1):

                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)
            # if the array a contains only 1 element then that element will be printed in the corresponding table
            if (len(a) == 1):
                table[row][col] = a[0]
    k = k - 1

print(table)