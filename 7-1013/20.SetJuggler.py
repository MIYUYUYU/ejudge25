

def get_union_of_sets(set_names, sets_dict):
    """获取多个集合的并集"""
    result = set()
    names = set_names.split(',')
    for name in names:
        if name in sets_dict:
            result.update(sets_dict[name])
    return result


def execute_command(command, sets):
    tokens = command.split()

    if tokens[0] == 'print':
        # print 集合名1,集合名2,...
        set_names = tokens[1]
        union_set = get_union_of_sets(set_names, sets)
        sorted_elements = sorted(union_set)
        print(' '.join(sorted_elements))

    elif tokens[0] == 'search':
        if tokens[2] == 'where':
            # search 源集合 where 字符串 to 新集合名
            source_names = tokens[1]
            search_string = tokens[3]
            new_set_name = tokens[5]

            source_union = get_union_of_sets(source_names, sets)
            result = {word for word in source_union if search_string in word}
            sets[new_set_name] = result

        elif tokens[2] == 'for':
            # search 源集合 for 搜索集合 to 新集合名
            source_names = tokens[1]
            search_names = tokens[3]
            new_set_name = tokens[5]

            source_union = get_union_of_sets(source_names, sets)
            search_union = get_union_of_sets(search_names, sets)

            result = source_union & search_union  # 交集
            sets[new_set_name] = result

words = []
while True:
    line = input().strip()
    if line == '':
        break
    words.extend(line.split())

# 初始化集合
sets = {'ALL': set(words)}

# 读取程序
program = []
while True:
    line = input().strip()
    if line == '':
        break
    program.append(line)

# 执行程序
for command in program:
    execute_command(command, sets)
