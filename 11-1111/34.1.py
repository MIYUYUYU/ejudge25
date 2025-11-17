class Sequence:
    def __init__(self, obj = None):
        self._sequence = []
        if obj is not None:
            self.sequence = obj

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        if hasattr(value, '__getitem__'):
            self._sequence = value
        else:
            self._sequence = [value]

    @sequence.deleter
    def sequence(self):
        empty = type(self._sequence)()
        self._sequence = empty

M, N = 25000, 1000
array = []
for i in range(N):
    array.append(Sequence(list(range(i, i + M))))
    del array[-1].sequence
print({type(seq.sequence) for seq in array})