class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed = ()):
        allowed_exception = False
        for tuple_test in suite:
            try:
                self.fun(*tuple_test)
            except Exception as e:
                #print(*allowed)
                if any(isinstance(e, allowed_ele) for allowed_ele in allowed):
                    allowed_exception = True
                else:
                    return 1
        return -1 if allowed_exception else 0

# T = Tester(int)
# print(T([(12,), ("12", 16)], []))
# print(T([(12,), ("12", 16), ("89", 8)], [ValueError, IndexError]))
# print(T([(12,), ("12", 16), ("89", 8), (1, 1, 1)], [ValueError, IndexError]))

# from math import log
# T = Tester(log)
# print(T(((i,) for i in range(1, 5))))
# print(T(((i,) for i in range(5))))
# print(T(((i,) for i in range(5)), [ValueError]))
# print(T(((i,) for i in range(5)), [Exception]))
# print(T(range(5), [ValueError]))