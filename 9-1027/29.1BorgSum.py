import weakref

class Borg:
    _isinstance = []
    def __init__(self, n = 0):
        self._n = n
        self._isinstance.append(weakref.ref(self))

    def __str__(self):
        return str(self._n)

    def __iadd__(self, number):
        for item in self._isinstance:
            if item is not None:
                item()._n += number
        return self

    def __isub__(self, number):
        for item in self._isinstance:
            if item is not None:
                item()._n -= number
        return self

    def __iter__(self):
        real_item = []
        for item in self._isinstance:
            #print(item())
            if item() is not None:
                real_item.append(item()._n)
        return iter(real_item)

# 测试代码
a, b, c = Borg(5), Borg(10), Borg(16)
print(a, b, c)  # 输出: 5 10 16
print(*a)  # 输出: 5 10 16
b += 10
c -= 1
print(*a)  # 输出: 14 19 25
del b
print(*a)  # 输出: 14 25

