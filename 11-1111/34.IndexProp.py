class Sequence:
    def __init__(self, obj = []):
        self._sequence = obj
        if obj != [] and hasattr(obj, '__getitem__'):
            self.sequence = obj
        elif obj != []:
            self.sequence = [obj]
    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value):
        self._sequence = value

    @sequence.deleter
    def sequence(self):
        self._sequence = type(self._sequence)()

# for obj in "qwe", {1:2, 3:4, 0:100}, None:
#     ins = Sequence(obj)
#     print(ins.sequence[0])
#     del ins.sequence
#     print(repr(ins.sequence))