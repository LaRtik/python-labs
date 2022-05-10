from abc import ABC, abstractmethod
import inspect
from types import FunctionType, CodeType


class SimplePickler(ABC):
    primitive_types = (int, float, str, bytes, bool)
    non_primitive_types = (list, set, frozenset, tuple, dict)
    code_args = ("argcount", "posonlyargcount", "kwonlyargcount", "nlocals", "stacksize", "flags", "code", "consts",
                 "names", "varnames", "filename", "name", "firstlineno", "lnotab", "freevars", "cellvars")

    @classmethod
    def get_code_attr(cls, fun_members):
        code_dict = dict([(arg, fun_members["co_" + arg]) for arg in cls.code_args])
        return CodeType(*[code_dict[arg] for arg in cls.code_args])

    @classmethod
    def get_dict_code(cls, fun_code):
        return dict([(arg, getattr(fun_code, "co_" + arg)) for arg in cls.code_args])

    @classmethod
    def dumps(cls, obj):
        obj_dict = dict()
        if inspect.isclass(obj):
            pass
        elif inspect.ismethod(obj):
            pass
        elif inspect.ismodule(obj):
            obj_dict = {
                "obj_type": type(obj).__name__,
                "obj_value": obj.__name__
            }
        elif inspect.iscode(obj):
            obj_dict = {
                "obj_type": type(obj).__name__,
                "obj_value": cls.dumps((cls.get_dict_code(obj)))
            }
        elif inspect.isfunction(obj):
            fun_members = dict(inspect.getmembers(obj))
            fun_code_attr = cls.get_code_attr(dict(inspect.getmembers(fun_members["__code__"])))
            fun_name = fun_members["__name__"]
            fun_globals = {key: value for key, value in fun_members["__globals__"].items() if not inspect.isclass(
                value) and not inspect.ismethod(value) and not inspect.isfunction(value)}
            for glob in fun_code_attr.co_names:
                if glob in fun_members["__globals__"]:
                    fun_globals.update({glob: fun_members["__globals__"][glob]})
            fun_defaults = fun_members["__defaults__"]
            obj_dict = {
                "obj_type": type(obj).__name__,
                "obj_value": cls.dumps(list([fun_code_attr, fun_globals, fun_name, fun_defaults, obj.__closure__]))
            }
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
        value = {}
        if obj_dict.get("obj_type"):
            value = obj_dict["obj_type"]
        else:
            return None
        if value in (item.__name__ for item in cls.primitive_types):
            for typ in cls.primitive_types:  # if primitive
                if value == typ.__name__:
                    return typ(obj_dict["obj_value"])

        elif value in (item.__name__ for item in cls.non_primitive_types):
            for typ in cls.non_primitive_types:  # if non primitive
                if value == typ.__name__:
                    return typ(cls.loads(item) for item in obj_dict["obj_value"])

        elif value == "code":
            code_dict = cls.loads(obj_dict["obj_value"])
            return CodeType(*[code_dict[arg] for arg in cls.code_args])

        elif value == "module":
            return __import__(obj_dict["obj_value"])

        elif value == "function":
            malist = obj_dict["obj_value"]
            arguments = cls.loads(obj_dict["obj_value"])
            return FunctionType(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])
