table = [[1 for i in range(4)] for j in range(4)]
for i in range (4):
    for j in range (4):
        print("Enter the value of ",i,j,":")
        table[i][j]=input("")
print(table)
i=2
while(i!=0):
    for row in range(4):
        for col in range(4):
            a = [1, 2, 3, 4]
            if (table[row][col] == '0'):
                print("")
                print(row, col)
                for i in table[row][:]:
                    print(i, end="    ")
                    b = int(i)
                    if (b in a):
                        a.remove(b)
                        print(a)
                for j in range(4):
                    print(table[j][col], end="    ")
                    c = int(table[j][col])
                    if (c in a):
                        a.remove(c)
                        print(a)
                if ((row + 1) % 2 == 1):
                    if ((col + 1) % 2 == 1):
                        print("")
                        for i in range(2):
                            for j in range(2):
                                print(table[row + i][col + j])
                                d = int(table[row + i][col + j])
                                if (d in a):
                                    a.remove(d)
                                    print(a)

                    elif ((col + 1) % 2 == 0):
                        print("")
                        for i in range(2):
                            for j in range(-1, 1):
                                print(table[row + i][col + j])
                                e = int(table[row + i][col + j])
                                if (e in a):
                                    a.remove(e)
                                    print(a)
                elif ((row + 1) % 2 == 0):
                    if ((col + 1) % 2 == 1):
                        print("")
                        for i in range(-1, 1):
                            for j in range(2):
                                print(table[row + i][col + j])
                                f = int(table[row + i][col + j])
                                if (f in a):
                                    a.remove(f)
                                    print(a)
                    elif ((col + 1) % 2 == 0):
                        print("")
                        for i in range(-1, 1):
                            for j in range(-1, 1):
                                print(table[row + i][col + j])
                                g = int(table[row + i][col + j])
                                if (g in a):
                                    a.remove(g)
                                    print(a)

                print(a[0])
                print(len(a))
                if (len(a) == 1):
                    print("keri")
                    table[row][col] = a[0]
                for i in table[row][:]:
                    print(i, end="    ")
    i=i-1

print(table)
