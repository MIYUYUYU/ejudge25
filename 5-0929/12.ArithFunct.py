from math import *
#def SUB()
def crea_opera(operation):
    def operator(f, g):
        def h(x):
            f_value = f(x) if callable(f) else f
            g_value = g(x) if callable(g) else g
            return operation(f_value, g_value)
        return h
    return operator

SUB = crea_opera(lambda x, y: x - y)
DIV = crea_opera(lambda x, y: x / y)
ADD = crea_opera(lambda x, y: x + y)
MUL = crea_opera(lambda x, y: x * y)

# f = SUB(sin, cos)
# print(f(12), sin(12)-cos(12))
#
# g = DIV(sin, cos)
# print(g(pi/6), tan(pi/6))
#
# h = MUL(exp, 0.1)
# print(h(2), e**2/10)
#
# t = ADD(len, sum)
# print(t(range(5)))