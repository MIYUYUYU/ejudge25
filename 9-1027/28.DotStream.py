class Dots:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __getitem__(self, key):
        if isinstance(key, int):
            return (self.start + (self.end - self.start)/(key-1) * i for i in range(key))
        elif isinstance(key, slice):
            if key.step is None:
                point = key.start
                n = key.stop
                #print(key.start, key.stop)
                return (self.start + (self.end - self.start)/(n-1) * point)
            else:
                #print(1)
                start = 0 if key.start is None else key.start
                end = key.step if key.stop is None else key.stop
                n = key.step
                return (self.start + (self.end - self.start)/(n-1) * i for i in range(start, end))


# W = 2 ** 48
# a = Dots(0, W * 2)
# print(a[W - 1:W + 1])
# print(next(a[1:W - 1:W + 1]))
# a = Dots(0,40)
# print(*a[5])
# print(a[0:5])
# print(a[2:5])
# print(a[4:5])
# print(a[7:5])
# print(a[-7:5])
# print(*a[1:3:5])
# print(*a[:3:5])
# print(*a[2::5])
# print(*a[::5])
# print(*a[-2:6:5])
