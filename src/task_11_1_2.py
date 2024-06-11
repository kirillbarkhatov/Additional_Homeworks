with open("nums.txt", "r") as f:
    rows = [row.rstrip() for row in f]
    for row in range(len(rows)):
        for i in range(len(rows[row])):
            if rows[row][i] == '#':
                rows[row] = rows[row][:i]
                break

    rows = list(filter(lambda x:not(x=="nan" or x=="inf" or x=="-inf"), rows))
    rows = [int(i) for i in rows if i != ""]
    rows = [(i+abs(i))/2 for i in rows]
    print(f'the sum is {sum(rows)}')