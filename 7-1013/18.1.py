def evalform(formula, *args):
    variable = []
    current_var = ""
    for char in formula:
        if char.isalpha():
            current_var += char
        else:
            if current_var:
                variable.append(current_var)
                current_var = ""
    # 只在 current_var 不为空时添加
    if current_var:
        variable.append(current_var)

    sorted_variable = sorted(set(variable))
    var_dic = dict(zip(sorted_variable, args))
    return eval(formula, {}, var_dic)  # 使用空的 globals


# 测试
print(eval(input()))  # 应该只输出 42