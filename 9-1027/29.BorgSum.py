import weakref
class Borg:
    _instances = []  # 存储弱引用的列表

    def __init__(self, value=0):
        self.value = value
        # 创建弱引用并添加到列表
        weak_ref = weakref.ref(self)
        self._instances.append(weak_ref)

    def __str__(self):
        return str(self.value)

    def __iter__(self):
        # 返回所有存活实例的值的迭代器
        alive_values = []
        for weak_ref in self._instances:
            instance = weak_ref()  # 获取弱引用指向的实际对象
            if instance is not None:  # 确保实例仍然存在
                alive_values.append(instance.value)

        return iter(alive_values)

    def __iadd__(self, other):
        # 对所有实例的值加上指定的数
        for weak_ref in self._instances:
            instance = weak_ref()
            if instance is not None:  # 确保实例仍然存在
                instance.value += other
        return self

    def __isub__(self, other):
        # 对所有实例的值减去指定的数
        for weak_ref in self._instances:
            instance = weak_ref()
            if instance is not None:  # 确保实例仍然存在
                instance.value -= other
        return self


# # 测试代码
# a, b, c = Borg(5), Borg(10), Borg(16)
# print(a, b, c)  # 输出: 5 10 16
# print(*a)  # 输出: 5 10 16
# b += 10
# c -= 1
# print(*a)  # 输出: 14 19 25
# del b
# print(*a)  # 输出: 14 25