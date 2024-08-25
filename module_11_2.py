import inspect


def introspection_info(obj):
    res = {}
    methods = []
    attrs = []
    type_list = [int, str, bool, list, tuple, dict, float, set]
    for i in dir(obj):
        attr = getattr(obj, i)
        if type(attr) in type_list:
            attrs.append(i)
        else:
            methods.append(i)
    res['type'] = type(obj)
    res['attributes'] = attrs
    res['methods'] = methods
    res['module'] = inspect.getmodule(type(obj))
    return res


class Testing:
    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def method_1(self):
        pass

    def method_2(self):
        pass


object_1 = Testing(1, True)
object_2 = 'string'
object_3 = 42

print(introspection_info(object_1))
print(introspection_info(object_2))
print(introspection_info(object_3))
