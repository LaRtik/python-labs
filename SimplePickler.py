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
        tempo = cls.pre_dumps(obj)
        return cls.format(cls.pre_dumps(obj))

    @classmethod
    def dump(cls, fp, obj):

        return fp.write(cls.dumps(obj))

    @classmethod
    def pre_dumps(cls, obj):
        obj_dict = {
            "obj_type": type(obj).__name__
        }
        if inspect.isclass(obj):  # is class type
            ignored_fields = ("__dict__", "__weakref__")
            members = {key: value for key, value in dict(obj.__dict__).items() if key not in ignored_fields}
            obj_dict["obj_value"] = cls.pre_dumps(members)

        elif inspect.ismethod(obj):  # is method type
            pass

        elif inspect.ismodule(obj):  # is module type
            obj_dict["obj_value"] = obj.__name__

        elif inspect.iscode(obj):  # is code type
            obj_dict["obj_value"] = cls.pre_dumps((cls.get_dict_code(obj)))

        elif inspect.isfunction(obj):  # is function type
            fun_members = dict(inspect.getmembers(obj))
            fun_code_attr = cls.get_code_attr(dict(inspect.getmembers(fun_members["__code__"])))
            fun_name = fun_members["__name__"]
            fun_globals = {key: value for key, value in fun_members["__globals__"].items() if not inspect.isclass(
                value) and not inspect.ismethod(value) and not inspect.isfunction(value)}
            for glob in fun_code_attr.co_names:  # only add globals that are used in that func
                if glob in fun_members["__globals__"]:
                    fun_globals.update({glob: fun_members["__globals__"][glob]})
            fun_defaults = fun_members["__defaults__"]
            obj_dict["obj_value"] = cls.pre_dumps(
                list([fun_code_attr, fun_globals, fun_name, fun_defaults, obj.__closure__]))

        elif isinstance(obj, cls.primitive_types):  # is primitive type
            if obj == "formatted":
                print("BUG HERE")
            obj_dict["obj_value"] = obj

        elif isinstance(obj, cls.non_primitive_types):  # is non-primitive type
            if isinstance(obj, dict):
                obj = list(tuple([key, value]) for key, value in obj.items())
            obj_dict["obj_value"] = tuple(cls.pre_dumps(item) for item in obj)

        else:
            return {}

        return obj_dict

    @abstractmethod
    def format(self, obj_dict):
        pass

    @abstractmethod
    def restore(self, obj_dict_formatted):
        pass

    @classmethod
    def loads(cls, obj_str):
        obj_dict = cls.restore(obj_str)
        return cls.post_loads(obj_dict)

    @classmethod
    def post_loads(cls, obj_dict):
        if not isinstance(obj_dict, dict):
            return None
        value = {}
        if obj_dict.get("obj_type"):
            value = obj_dict["obj_type"]
        else:
            return None

        if value in (item.__name__ for item in cls.primitive_types):  # if object is a primitive type
            for typ in cls.primitive_types:  # if primitive
                if value == typ.__name__:
                    if value == "bytes":
                        obj_dict["obj_value"] = obj_dict["obj_value"].to_bytes((obj_dict["obj_value"].bit_length()  +
                                                                                7) // 8, "big")
                    return typ(obj_dict["obj_value"])

        elif value in (item.__name__ for item in cls.non_primitive_types):  # if object is not a primitive_type
            for typ in cls.non_primitive_types:  # if non primitive
                if value == typ.__name__:
                    objects = list()
                    if not isinstance(obj_dict["obj_value"], tuple):
                        objects.append(obj_dict["obj_value"])
                    else:
                        objects = obj_dict["obj_value"]
                    return typ(cls.post_loads(item) for item in objects)

        elif value == "code":  # if code type
            code_dict = cls.post_loads(obj_dict["obj_value"])
            return CodeType(*[code_dict[arg] for arg in cls.code_args])

        elif value == "module":  # if module type
            return __import__(obj_dict["obj_value"])

        elif value == "function":  # is function type
            arguments = cls.post_loads(obj_dict["obj_value"])
            return FunctionType(arguments[0], arguments[1], arguments[2], arguments[3], arguments[4])

        elif value == "type":  # is class type
            members = cls.post_loads(obj_dict["obj_value"])
            return type("Dumped Class", (), members)
