
rectangles = []
while True:
    try:
        line = input().strip()
        if line == '':
            break
        parts = line.split()
        if len(parts) < 5:
            continue
        x = int(parts[0])
        y = int(parts[1])
        w = int(parts[2])
        h = int(parts[3])
        char = parts[4]
        rectangles.append((x, y, w, h, char))
    except EOFError:
        break


min_x = float('inf')
max_x = float('-inf')
min_y = float('inf')
max_y = float('-inf')

for rect in rectangles:
    x, y, w, h, char = rect
    if w > 0:
        x1 = x
        x2 = x + w - 1
    elif w < 0:
        x1 = x + w
        x2 = x - 1
    else:
        x1 = x2 = x

    if h > 0:
        y1 = y
        y2 = y + h - 1
    elif h < 0:
        y1 = y + h
        y2 = y - 1
    else:
        y1 = y2 = y

    if w != 0:
        min_x = min(min_x, x1)
        max_x = max(max_x, x2)
    if h != 0:
        min_y = min(min_y, y1)
        max_y = max(max_y, y2)

if min_x == float('inf'):
    min_x = 0
    max_x = 0
if min_y == float('inf'):
    min_y = 0
    max_y = 0
print(float('inf'))
width = max_x - min_x + 1
height = max_y - min_y + 1

grid = [['.'] * width for _ in range(height)]

for rect in rectangles:
    x, y, w, h, char = rect
    if w > 0:
        x1 = x
        x2 = x + w - 1
    elif w < 0:
        x1 = x + w
        x2 = x - 1
    else:
        continue

    if h > 0:
        y1 = y
        y2 = y + h - 1
    elif h < 0:
        y1 = y + h
        y2 = y - 1
    else:
        continue

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if min_x <= i <= max_x and min_y <= j <= max_y:
                col = i - min_x
                row = j - min_y
                grid[row][col] = char

for row in grid:
    print(''.join(row))