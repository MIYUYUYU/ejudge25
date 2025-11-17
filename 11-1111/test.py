class ParDescr:
    def __init__(self, initial_value):
        self.initial_value = initial_value
        self._values = {}

    def __get__(self, instance, owner):
        print(f"__get__被调用，instance={instance}")
        if instance is None:
            return self.initial_value
        else:
            # 如果实例还没有存储值，就返回初始值
            return self._values.get(instance, self.initial_value)

    def __set__(self, instance, value):
        print(f"__set__被调用，设置值为: {value}")
        self._values[instance] = value


class MyClass:
    attr = ParDescr("默认初始值")  # 描述符被定义，但尚未赋值