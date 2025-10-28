def itercalc():
    stack = []
    result = None
    cmd = yield result  # 初始化，等待第一个命令

    while True:
        # 处理 "?" 命令 - 返回栈顶元素
        if cmd == "?":
            if stack:
                result = stack[-1]
            else:
                print("Insufficient stack")
                result = None

        # 处理运算符命令
        elif cmd in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                print("Insufficient stack")
                result = None
            else:
                b = stack.pop()
                a = stack.pop()

                try:
                    if cmd == "+":
                        res = a + b
                    elif cmd == "-":
                        res = a - b
                    elif cmd == "*":
                        res = a * b
                    elif cmd == "/":
                        if b == 0:
                            raise ZeroDivisionError
                        res = a // b  # 整数除法

                    stack.append(res)
                    result = None
                except ZeroDivisionError:
                    print("Zero division")
                    # 恢复栈状态
                    stack.append(a)
                    stack.append(b)
                    result = None

        # 处理其他命令
        else:
            try:
                # 尝试解析为整数
                num = int(cmd)
                stack.append(num)
                result = None
            except ValueError:
                # 不是整数，也不是已知命令
                print("Unknown command")
                result = None

        # 等待下一个命令并返回结果
        cmd = yield result

# calc = itercalc()
# next(calc)
# for cmd in "? 3 -2 - what 5 * 2 / ?".split():
#     if (res := calc.send(cmd)) is not None:
#         print(res)