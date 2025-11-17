from itertools import product
from string import ascii_lowercase

def slotgen(number):
    def decorator(cls):
        i = 1
        while 26 ** i < number:
            i += 1
        alphabet = list(ascii_lowercase)
        items = product(alphabet, repeat=i)
        slot_cls = []
        count_slot = 0
        for item in items:
            slot_cls.append(''.join(item))
            count_slot += 1
            if count_slot >= number:
                break
        cls_prop = {}
        for name in dir(cls):
            if not name.startswith('__') and name not in slot_cls:
                cls_prop[name] = getattr(cls, name)

        class new_slot():
            __slots__ = slot_cls

            def __setattr__(self, name, value):
                if name in cls_prop or name not in slot_cls:
                    raise AttributeError(f"can't set attribute {name}")
                else:
                    super().__setattr__(name, value)

            pass
        for name, value in cls_prop.items():
            setattr(new_slot, name, value)
        return new_slot
    return decorator


# @slotgen(29)
# class C:
#     field = 12
#     ab = 100500
#
# c = C()
# c.ba = 100500
# for attr in "aa ab field ba".split():
#     try:
#         print(f"{attr}={getattr(c, attr)}")
#     except AttributeError:
#         print(f"No {attr}")