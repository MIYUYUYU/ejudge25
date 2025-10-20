import math
list_gal = []
while True:
    inp = input().strip()
    if inp == '' or inp=='.':
        break
    inp_list = [float(x.strip()) if i in [0,1,2] else x.strip() for i,x in enumerate(inp.split(' '))]
    list_gal.append(inp_list)
    #print(inp_list)

#print(list_gal)
max_dist = float('-inf')
index_maxi = 0
index_maxj = 1
for i in range(len(list_gal)):
    for j in range(i,len(list_gal)):
        x1, y1, z1, name1 = list_gal[i][0], list_gal[i][1], list_gal[i][2], list_gal[i][3]
        x2, y2, z2, name2 = list_gal[j][0], list_gal[j][1], list_gal[j][2], list_gal[j][3]
        dist = math.dist((x1,y1,z1),(x2,y2,z2))
        if  dist > max_dist:
            index_maxi = i
            index_maxj = j
            max_dist = dist
max_pair = sorted([list_gal[index_maxi][3],list_gal[index_maxj][3]])

print(f"{max_pair[0]} {max_pair[1]}")
