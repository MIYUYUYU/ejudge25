def pastri(n,filler):
    tri = [[1]]
    for i in range(1,n):
        row = [1]

        if i >= 2:
            for j in range(1,i):
                row.append(tri[i-1][j-1]+tri[i-1][j])
        row.append(1)
        tri.append(row)
        #print(tri)
    pro_tri = []
    for row in tri:
        pro_tri.append(filler.join(str(x) for x in row))

    out_tri = []
    for row in pro_tri:
        sub_len = len(pro_tri[n - 1]) - len(row)
        if sub_len % 2 == 0:
            new_row = filler*(sub_len//2) + row + filler*(sub_len//2)
        else:
            new_row = filler*(sub_len//2) + row + filler*(sub_len//2 + 1)
        out_tri.append(new_row)

    return '\n'.join(out_tri)

#print(pastri(2,'_'))