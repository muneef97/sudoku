def str_arr_to_int_arr(str_arr):
    int_arr = []
    for i in str_arr:
        int_arr.append(int(i))
    return int_arr

def read_input(file):
    f = open(file, "r")
    table = []
    for line in open('input.txt', 'r'):
        table.append(str_arr_to_int_arr(line.strip().split(",")))
    print(table)
    return table

def write_output(file,table):
    f = open(file, "w")
    for i in table:
        a = ",".join(str(x) for x in i)
        f.write(a)
        f.write("\n")
    return table

def remove_element(table,row_begin,row_end,col_begin,col_end,table_row,table_col,a):
    for i in range(row_begin,row_end):
        for j in range(col_begin,col_end):

            d = int(table[table_row + i][table_col + j])
            if (d in a):
                a.remove(d)
    return a

def solve_sudo_ku(table):
    k=4
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

                            remove_element(table,0,3,0,3,row,col,a)

                        # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                        # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                        elif ((col + 1) % 3 == 2):

                            remove_element(table, 0, 3, -1, 2, row, col, a)

                        # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                        # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                        elif ((col + 1) % 3 == 0):
                            # print("")
                            remove_element(table, 0, 3, -2, 1, row, col, a)

                    # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                    # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                    if ((row + 1) % 3 == 2):

                        if ((col + 1) % 3 == 1):

                            remove_element(table, -1, 2, 0, 3, row, col, a)

                        # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                        # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                        elif ((col + 1) % 3 == 2):

                            remove_element(table, -1, 2, -1, 2, row, col, a)
                        # if row % 3 = 2, then 3x3 boxes will be row-1 , row, row+1
                        # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                        elif ((col + 1) % 3 == 0):

                            remove_element(table, -1, 2, -2, 1, row, col, a)

                    # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                    # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                    if ((row + 1) % 3 == 0):
                        if ((col + 1) % 3 == 1):

                            remove_element(table, -2, 1, 0, 3, row, col, a)

                        # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                        # if col % 3 = 2 , then 3x3 boxes will be, col-1, col, col+1
                        elif ((col + 1) % 3 == 2):

                            remove_element(table, -2, 1, -1, 2, row, col, a)

                        # if row % 3 = 0, then 3x3 boxes will be row-2 , row-1, row
                        # if col % 3 = 0 , then 3x3 boxes will be, col-2, col-1, col
                        elif ((col + 1) % 3 == 0):

                            remove_element(table, -2, 1, -2, 1, row, col, a)

                # if the array a contains only 1 element then that element will be printed in the corresponding table
                if (len(a) == 1):
                    table[row][col] = a[0]
        k = k - 1
    print(table)
    return table

table=read_input("input.txt")
solution=solve_sudo_ku(table)
write_output("output.txt", solution)

