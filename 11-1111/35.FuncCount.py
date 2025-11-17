from functools import wraps
def counter(fun):
    count = 0
    @wraps(fun)

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return fun(*args, **kwargs)

    def counter_m():
        return count

    wrapper.counter = counter_m

    return wrapper

# @counter
# def fun(a, b):
#     return a * 1 + b
#
# # print(fun.counter())
# # res = sum(fun(i, i + 1) for i in range(5))
# # print(fun.counter(), res)
# #
