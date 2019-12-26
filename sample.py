def str_arr_to_int_arr(str_arr):
    int_arr = []
    for i in str_arr:
        int_arr.append(int(i))
    return int_arr

def read_input(file):
    f = open(file, "r")
    table = []
    for line in open(file, 'r'):
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

def remove_element_if_exists_in_a_3x3_block(table,row_begin,row_end,col_begin,col_end,table_row,table_col,array):
    for i in range(row_begin,row_end):
        for j in range(col_begin,col_end):
            d = int(table[table_row + i][table_col + j])
            if (d in array):
                array.remove(d)
    return array

def identify_3x3_block_and_remove(table,row,col,array):
    row_begin = -(row % 3)
    row_end = 3 - (row % 3)
    col_begin = 0 - (col % 3)
    col_end = 3- (col % 3)
    remove_element_if_exists_in_a_3x3_block(table, row_begin,row_end, col_begin, col_end, row, col, array)
    return array

def check_for_unsolved_elements(table):
    flag = 1
    for i in range(9):
        for j in range(9):
            if(table[i][j]==0):
                flag=0
    return flag



def solve_sudo_ku(table):
    flag = 0
    k=0
    while ( flag == 0):

        # This while loop is used to work the following processes in k times
        for row in range(9):
            for col in range(9):

                array = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Here elements in array is integer type
                if (table[row][col] == 0):  # Here checking the empty boxes, if it is zero the following program will work

                    for i in range(9):  # Checking elements in row and column
                        b = int(table[row][i])  # elements in the table are str type , so converting them to int type
                        if (b in array):  # since a and b are int type comparing them to remove b from a
                            array.remove(b)
                        c = int(table[i][col])
                        if (c in array):
                            array.remove(c)

                    # The following program is for identifying each 3x3 boxes for corresponding box,
                    # Let row and col indicate the row and column of the table where element is zero
                    # Then the corresponding 3x3 boxes will get as,
                    # if row % 3 = 1, then 3x3 boxes will be row , row+1, row+2
                    # if col % 3 = 1 , then 3x3 boxes will be, col, col+1, col+2
                    identify_3x3_block_and_remove(table, row, col, array)


                # if the array a contains only 1 element then that element will be printed in the corresponding table
                if (len(array) == 1):
                    table[row][col] = array[0]
        k = k + 1
        print("k=" + str(k))
        flag = check_for_unsolved_elements(table)

    print(table)
    return table

table=read_input("inputhard.txt")
solution=solve_sudo_ku(table)
write_output("output.txt", solution)

