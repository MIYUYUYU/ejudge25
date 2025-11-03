#坐标生成器
def coord_gen():
    yield (0,0)
    yield (1,0)
    yield (1,-1)
    yield (1, -2)
    x, y = 1, -2
    count_line = 3
    while True:
        for i in range(count_line):
            x -= 1
            yield (x,y)
        count_line += 1
        for i in range(count_line):
            y += 1
            yield (x,y)
        count_line += 1
        for i in range(count_line):
            x += 1
            yield (x,y)
        count_line += 1
        for i in range(count_line):
            y -= 1
            yield (x,y)
        count_line += 1

#输出格生成器，输入字符串，生成需要的逆时针字符串
def grid_gen(s):
    list_s = []
    coord = coord_gen()
    for i in range(len(s)):
        list_s.append((s[i],next(coord)))
    max_y = max(list_s, key=lambda x: x[1][1])[1][1]
    min_y = min(list_s, key=lambda x: x[1][1])[1][1]
    max_x = max(list_s, key=lambda x: x[1][0])[1][0]
    min_x = min(list_s, key=lambda x: x[1][0])[1][0]
    #print(f"max_x={max_x}, min_x={min_x} max_y={max_y}, min_y={min_y}")
    grid_y = max_y - min_y + 1
    grid_x = max_x - min_x + 1
    new_s = []
    # for i in range(len(s)):
    #     new_s.append((list_s[i][0],(list_s[i][1][0]+abs(min_x),list_s[i][1][1]+abs(min_y))))
    out_grid = [[' ']*grid_x for _ in range(grid_y)]
    #print(out_grid)
    #print(len(new_s))
    for i in range(len(s)):
        #print(f'a ={new_s[i][0]} x = {new_s[i][1][0]} y = {new_s[i][1][1]}')
        #print(f"before {out_grid[new_s[i][1][0]][new_s[i][1][1]]}")
        out_grid[list_s[i][1][1]+abs(min_y)][list_s[i][1][0]+abs(min_x)] = list_s[i][0]
        #print(f"after {out_grid[new_s[i][1][0]][new_s[i][1][1]]}")
    result = '\n'.join(''.join(row) for row in out_grid)
    #print(result)
    # print(list_s)
    # print(new_s)
    return result

from collections import OrderedDict
#获取排序后字符串
def order_str(s):
    odr_s = OrderedDict()
    for char in s:
        if char not in odr_s:
            odr_s[char] = 1
        else:
            odr_s[char] += 1
    out_s = []
    for key, value in odr_s.items():
        out_s.append(str(key)*value)
    result = ''.join(out_s)
    return result

#获取减法后的字典
def get_order_dicts_sub(s1, s2):
    order_dict_s = OrderedDict()
    for char in s1:
        if char not in order_dict_s:
            order_dict_s[char] = 1
        else:
            order_dict_s[char] += 1
    for char in s2:
        if char in s1:
            order_dict_s[char] -= 1
    result_dict = {k : v for k, v in order_dict_s.items() if v > 0}
    return result_dict

#字符串减法
def sub_str(s1, s2):
    dict_result = get_order_dicts_sub(s1, s2)
    out_s = []
    for key, value in dict_result.items():
        out_s.append(str(key) * value)
    result = ''.join(out_s)
    return result

class Spiral():
    def __init__(self, s):
            self.s = order_str(s)

    def __str__(self):
        return grid_gen(self.s)

    def __add__(self, other):
        result = self.s + other.s
        return Spiral(result)

    def __sub__(self, other):
        result = sub_str(self.s, other.s)
        return Spiral(result)

    def __mul__(self, number):
        result = self.s * number
        return Spiral(result)

    def __iter__(self):
        return iter(self.s)

# S = Spiral("abbcccddddeeeee")
# I = Spiral("abcdefghi")
# print(f'{S}\n')
# print(S+I, "\n")
# print(S-I, "\n")
# print(I*2, "\n")
# print(I*2-S, "\n")
# print(*list(S+I))
# import random, string
# random.seed(12345)
# A, B =(Spiral("".join(sorted(random.choices(string.ascii_letters, k=50000)))) for i in range(2))
# print(A+Spiral(""))
# print(B+Spiral("1"))
# print(Spiral("2")+A+B)
# print(Spiral("3")+A-B*2)
# print(B*2-A*3+Spiral("0"))
# print("".join(A)+"".join(B))