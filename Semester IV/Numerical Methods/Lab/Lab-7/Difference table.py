def difference_table(y_values):
    n = len(y_values)
    table = [y_values]

    for i in range(1, n):
        diff = []
        for j in range(n - i):
            diff.append(table[i-1][j+1] - table[i-1][j])
        table.append(diff)

    print("Forward Difference Table:")
    for i in range(n):
        for j in range(n - i):
            print(f"{table[i][j]:<10.4f}", end="\t")
        print()

y = [6,7,8,9]
difference_table(y)
