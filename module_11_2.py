import inspect
from pprint import pprint


def introspection_info(obj):
    res = {}

    res['type'] = type(obj)
    res['attributes'] = [*obj.__dict__.keys()]
    res['methods'] = [func for func in dir(obj)
                      if callable(getattr(obj, func))
                      and not func.startswith('__')]
    res['module'] = obj.__module__
    return res


class Testing:
    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def method_1(self):
        pass

    def method_2(self):
        pass


object_1 = Testing(1, 2)

print(introspection_info(object_1))