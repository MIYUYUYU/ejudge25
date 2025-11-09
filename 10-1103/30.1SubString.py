class SubString(str):
    def __new__(cls, s):
        return super().__new__(cls, s)

    def __sub__(self, other):
        counter = {}
        for char in other:
            counter[char] = counter.get(char, 0) + 1

        result = []

        for char in self:
            if char in counter and counter[char] > 0:
                counter[char] -= 1
            else:
                result.append(char)

        return SubString(''.join(result))

    def __getattribute__(self, name):
        if name.startswith('__') and name.endswith('__'):
            return super().__getattribute__(name)
        attr = super().__getattribute__(name)
        #print(type(attr))
        if hasattr(str, name) and callable(attr):
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                if isinstance(result, str):
                    return self.__class__(result)
                return result
            return wrapper
        return attr

    def __rmul__(self, other):
        return SubString(super().__rmul__(other))

    def __mul__(self, other):
        return SubString(super().__mul__(other))

    def __getitem__(self, index):
        return self.__class__(super().__getitem__(index))

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        return self.__class__(other) + self

    def __rsub__(self, other):
        return self.__class__(other) - self
# import sys
# inp = sys.stdin.read()
# exec(inp)

# import string
# N = 7000
# S1 = SubString("_".join(f"({x:04x}):" for x in range(N)))
# S2 = SubString( "_"*(N-3)+"():"*(N-2)+\
#         "0"*(N*5//4)+\
#         "123"*(N*10//45)+\
#         string.digits*(N//8)+\
#         string.ascii_lowercase*(N//5))
# print(S1-S2)

# A, B = SubString(list(range(5,15))), SubString(list(range(8,17)))
# print(f"{A} // {B}\n'{A-B}'//'{B-A}'")
# S, T = SubString(list(range(15,27))), SubString(tuple(range(20,55,3)))
# print(S)
# print(T)
# print(S-T, T-S)
# print(S*2-T*3)
# print(S[2:-2]-T[6:-6])
# print(S.replace(",",";")-T)
# print(S.replace(SubString(","),SubString("-=-"))-T)
# print(T.count(S[-6]))
# print(T[3:5] in S)