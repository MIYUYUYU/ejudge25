inp = []

while True:
    inp_row = [x.strip() for x in input().strip().split(' ')]
    if inp_row == ['']:
        break
    else:
        #print(f'{inp_row}')
        proc_row = list(map(int, inp_row[:4]))
        proc_row.append(inp_row[4])
        inp.append(proc_row)
max_x = float('-inf')
max_y = float('-inf')
min_x = float('inf')
min_y = float('inf')
#print(type(inp[0][0]))
for item in inp:
    x, y, w, h = item[:4]
    if w == 0 or h == 0:
        continue
    if w > 0:
        x1 = x + w - 1                  #x0 - min, x1 - max, y0 - min, y1 - max
        x0 = x
    if w < 0:
        x1 = x
        x0 = x + w
    if h > 0:
        y1 = y + h - 1
        y0 = y
    if h < 0:
        y1 = y
        y0 = y + h
    max_x = max(max_x, x1)
    max_y = max(max_y, y1)
    min_x = min(min_x, x0)
    min_y = min(min_y, y0)

print(f'max_x = {max_x} max_y = {max_y} min_x = {min_x} min_y = {min_y}')

#'.'append
out = []
for i in range(min_y, max_y + 1):
    out_row = []
    for j in range(min_x, max_x + 1):
        out_row.append('.')
    out.append(out_row)

for item in inp:
    x, y, w, h, char = item
    if w > 0:
        start_x = x - min_x
        end_x = x + w - min_x
    elif w < 0:
        start_x = x + w - min_x
        end_x = x - min_x
    else:  # w == 0
        continue

    if h > 0:
        start_y = y - min_y
        end_y = y + h - min_y
    elif h < 0:
        start_y = y + h - min_y
        end_y = y - min_y
    else:  # h == 0
        continue

    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            out[i][j] = char

print('\n'.join(''.join(row) for row in out))

