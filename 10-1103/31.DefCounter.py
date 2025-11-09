import collections

class DefCounter(collections.Counter):
    def __init__(self,str,missing= -1):
        super().__init__(str)
        self.missing = missing

    def __missing__(self, key):
        return self.missing

    def __abs__(self):
        result = 0
        for key in self:
            if self[key] > 0:
                result += self[key]
        return result

# A = DefCounter("QWEqweQWEqweQWE")
# print(A)
# A["P"] += 5
# print(A["T"], A["P"], abs(A), A.total())
# print(A)