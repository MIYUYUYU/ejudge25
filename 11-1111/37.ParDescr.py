import weakref
class ParDescr:
    def __init__(self, value):
        self._default_value = value
        self.value = {}

    def __set__(self, obj, value):
        self.value[obj] = value

    def __delete__(self,obj):
        if obj is not None:
            del self.value[obj]

    def __get__(self, obj, objtype=None):
        try:
            return self.value[obj]
        except KeyError:
            return self._default_value

# class C:
#     a = ParDescr(100500)
#     b = ParDescr(42)

# print(C.a, C.b)
# c, d = C(), C()
# print(c.a, c.b, d.a, d.b)
# c.a, d.b = "QQ", "QKRQ"
# print(c.a, c.b, d.a, d.b)
# del c.a
# print(c.a, c.b, d.a, d.b)