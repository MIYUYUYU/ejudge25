

def itercalc():
    stack = []
    result = None
    # cmd = yield result
    # print(f"cmd: {cmd}")
    cmd = yield result
    while True:
        #print(f"cmd: {cmd}")
        try:
            number = int(cmd)
            stack.append(number)
            result = None
        except ValueError:
            if cmd == '?':
                try:
                    result = stack[-1]
                except IndexError:
                    print("Insufficient stack")
                    result = None
            elif cmd in ('+','-','*','/'):
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    try:
                        if cmd == '+':
                            tmp = a + b
                        elif cmd == '-':
                            tmp = a - b
                        elif cmd == '*':
                            tmp = a * b
                        elif cmd == '/':
                            if b == 0:
                                raise ZeroDivisionError
                            tmp = a // b
                        #print(f"tmp = {tmp}")
                        stack.append(tmp)
                        result = None
                    except ZeroDivisionError:
                        print("Zero division")
                        stack.append(a)
                        stack.append(b)
                        result = None
                else:
                    print("Insufficient stack")
                    result = None

            else:
                print("Unknown command")
                result = None
            #print(f"result: {result}")
            #print(result)
        cmd = yield result
# calc = itercalc()
# next(calc)
# for cmd in "? 3 -2 - what 5 * 2 / ?".split():
#     if (res := calc.send(cmd)) is not None:
#         print(res)

# import random
# import sys
# from collections import Counter
# from io import StringIO
# def commands(length, args=2, prints=.25, diap=range(-99, 100)):
#     for i in range(length):
#         pprob = i * prints * 2 / length
#         if random.random() < pprob:
#             yield "?"
#         elif random.randrange(args + 1) == args:
#             yield random.choice("+-*/")
#         else:
#             yield str(random.choice(diap))
#
#
# random.seed(0xbadfed)
# calc = itercalc()
# stdout, sys.stdout = sys.stdout, StringIO("")
# next(calc)
# C = Counter(calc.send(cmd) for cmd in commands(100000))
# print(C.most_common()[:-20-1:-1], file=stdout)
# print(Counter(sys.stdout.getvalue().split()), file=stdout)
# import random
# from collections import Counter
#
# def commands(length, args=2, prints=.25, diap=range(-99, 100)):
#     for i in range(length):
#         pprob = i * prints * 2 / length
#         if random.random() < pprob:
#             yield "?"
#         elif random.randrange(args + 1) == args:
#             yield random.choice("+-*/")
#         else:
#             yield str(random.choice(diap))
#
#
# random.seed(1337)
# calc = itercalc()
# next(calc)
# print(Counter(calc.send(cmd) for cmd in commands(20000)))