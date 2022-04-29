from abc import ABC, abstractmethod
import inspect


class SimplePickler(ABC):
    primitive_types = (int, float, str, bytes, bool)
    non_primitive_types = (list, set, frozenset, tuple, dict)

    @classmethod
    def dumps(cls, obj: object):
        obj_dict = dict()
        if inspect.isclass(obj):
            pass
        elif inspect.ismethod(obj):
            pass
        elif isinstance(obj, cls.primitive_types):
            obj_dict = {
                "obj_type": type(obj).__name__,
                "obj_value": obj
            }
        elif isinstance(obj, cls.non_primitive_types):
            obj_dict = {
                "obj_type": type(obj).__name__,
            }
            if isinstance(obj, dict):
                obj = list(tuple([key, value]) for key, value in obj.items())
            obj_dict.update({"obj_value": tuple(cls.dumps(item) for item in obj)})
        return cls.format(obj_dict)

    @abstractmethod
    def format(self, obj_dict):
        pass

    @abstractmethod
    def restore(self, obj_dict_formatted):
        pass

    @classmethod
    def loads(cls, obj_dict_formatted):
        obj_dict = cls.restore(obj_dict_formatted)
        value = obj_dict["obj_type"]
        for typ in cls.primitive_types:  # if primitive
            if value == typ.__name__:
                return typ(obj_dict["obj_value"])

        for typ in cls.non_primitive_types:  # if non primitive
            if value == typ.__name__:
                return typ(cls.loads(item) for item in obj_dict["obj_value"])
