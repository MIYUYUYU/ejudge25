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

        if callable(attr) and hasattr(str, name):
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                return self.__class__(result)
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

    # def center(self, *args, **kwargs):
    #     return self.__class__(super().center(*args, **kwargs))
    #
    # def strip(self, *args, **kwargs):
    #     return self.__class__(super().strip(*args, **kwargs))

S=SubString
print("guilty" in S("Suspicion always haunts the guilty mind."))
print(S("guilty") in S("Suspicion always haunts the guilty mind."))
print(S("Suspicion").center(20, '.')-"pipi...")
print(S("__subclasshook__").strip("_")-"ice bus")
print(S("__subclasshook__").endswith("hook__"))