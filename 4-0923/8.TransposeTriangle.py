N = 0
tri = []
while (line := [x.strip() for x in input().split(',')]) != ['']:
    #print(line)
    tri.append(line)
    N += 1
new_tri = []
for j in range(N-1,-1,-1):
    line = []
    for i in range(j,N,1):
        line.append(tri[i][j])
 #       print(f'i = {i}, j = {j}, line = {line}')
    new_tri.append(line)
space = N-1
for line in new_tri:
    print(" "*space,end = '')
    space -= 1
    print(*line, sep=',')
#print(N)
